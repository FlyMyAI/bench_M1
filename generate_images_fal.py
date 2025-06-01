import asyncio
import fal_client
import json
import os
import time
import random
from tqdm import tqdm
import aiohttp

# Global counters (no threading needed for async version)
completed_count = 0
failed_count = 0

def increment_completed():
    global completed_count
    completed_count += 1

def increment_failed():
    global failed_count
    failed_count += 1

def get_counts():
    return completed_count, failed_count

def load_prompts_from_json(json_file):
    """Load prompts from JSON configuration file and organize them"""
    with open(json_file, 'r') as f:
        config = json.load(f)
    
    # Extract prompts organized by category
    organized_prompts = {}
    
    for category_name, category_data in config['categories'].items():
        category_prompts = []
        prompt_metadata = []
        
        # Collect prompts from all intensity levels
        for intensity_level in ['intensity_1_subtle', 'intensity_2_moderate', 'intensity_3_intense']:
            for prompt_data in category_data[intensity_level]:
                category_prompts.append(prompt_data['prompt'])
                prompt_metadata.append({
                    'id': prompt_data['id'],
                    'intensity': intensity_level,
                    'expected_difficulty': prompt_data['expected_difficulty']
                })
        
        organized_prompts[category_name] = {
            'prompts': category_prompts,
            'metadata': prompt_metadata
        }
    
    return organized_prompts, config

async def upload_and_edit_image(input_image_path, prompt, output_path, max_retries=3):
    """Upload image to fal.ai and edit it using bagel/edit model"""
    
    # Skip if output already exists
    if os.path.exists(output_path):
        print(f"Skipping {output_path} - already exists")
        return True
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    for attempt in range(max_retries):
        try:
            # Upload image to fal.ai storage
            print(f"Uploading {os.path.basename(input_image_path)}...")
            image_url = await fal_client.upload_file_async(input_image_path)
            print(f"Image uploaded: {image_url}")
            
            # Submit async request to bagel/edit
            print(f"Submitting edit request with prompt: {prompt[:50]}...")
            handler = await fal_client.submit_async(
                "fal-ai/bagel/edit",
                arguments={
                    "prompt": prompt,
                    "image_url": image_url
                },
            )
            
            # Optional: Listen to events (shows progress)
            print("Processing...")
            async for event in handler.iter_events(with_logs=False):
                if hasattr(event, 'type'):
                    print(f"Event: {event.type}")
            
            # Get the final result
            result = await handler.get()
            print(f"Result received")
            
            # Extract and download the generated image
            generated_image_url = None
            
            if isinstance(result, dict) and "image" in result:
                # Handle single image response
                if isinstance(result["image"], dict) and "url" in result["image"]:
                    generated_image_url = result["image"]["url"]
                elif isinstance(result["image"], str):
                    generated_image_url = result["image"]
                    
            elif isinstance(result, dict) and "images" in result and result["images"]:
                # Handle multiple images response
                first_image = result["images"][0]
                if isinstance(first_image, dict) and "url" in first_image:
                    generated_image_url = first_image["url"]
                elif isinstance(first_image, str):
                    generated_image_url = first_image
            
            if not generated_image_url:
                print(f"No image URL found in result: {result}")
                continue
            
            # Download the generated image
            print(f"Downloading result...")
            async with aiohttp.ClientSession() as session:
                async with session.get(generated_image_url) as response:
                    if response.status == 200:
                        content = await response.read()
                        with open(output_path, 'wb') as f:
                            f.write(content)
                        print(f"Successfully saved: {os.path.basename(output_path)}")
                        return True
                    else:
                        print(f"Failed to download: HTTP {response.status}")
                        continue
                        
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = 15  # Fixed 15s wait time
                print(f"Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                print(f"Failed after {max_retries} attempts")
                return False
    
    return False

async def process_single_task(task_info):
    """Process a single task asynchronously"""
    img_file, img_path, category, prompt_idx, prompt, output_path, prompt_id = task_info
    
    success = await upload_and_edit_image(
        input_image_path=img_path,
        prompt=prompt,
        output_path=output_path,
        max_retries=60
    )
    
    if success:
        increment_completed()
    else:
        increment_failed()
        with open("failed_generations_fal_benchmark.log", "a") as f:
            f.write(f"{img_file},{category},{prompt_idx},{prompt_id},{prompt}\n")
    
    # Add delay between requests
    await asyncio.sleep(random.uniform(2.0, 4.0))
    return success, img_file, category, prompt_idx

async def process_batch_with_semaphore(tasks, max_concurrent=2):
    """Process tasks with concurrency control using semaphore"""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_with_semaphore(task):
        async with semaphore:
            return await process_single_task(task)
    
    # Create tasks with semaphore control
    task_coroutines = [process_with_semaphore(task) for task in tasks]
    
    # Process with progress bar
    results = []
    with tqdm(total=len(tasks), desc="Processing images") as pbar:
        for coro in asyncio.as_completed(task_coroutines):
            result = await coro
            results.append(result)
            
            # Update progress
            completed, failed = get_counts()
            success, img_name, cat, p_idx = result
            pbar.set_description(f"Processed {img_name} - {cat} prompt {p_idx}")
            pbar.set_postfix(completed=completed, failed=failed, concurrent=max_concurrent)
            pbar.update(1)
    
    return results

async def main():
    """Main async function to generate benchmark images using JSON prompts"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate benchmark images using FAL.ai and JSON prompts')
    parser.add_argument('--prompts_json', type=str, default='prompts_small.json',
                       help='Path to prompts JSON configuration file')
    parser.add_argument('--input_dir', type=str, 
                       help='Directory containing input FFHQ images')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory for generated images')
    parser.add_argument('--max_concurrent', type=int, default=2,
                       help='Maximum concurrent requests')
    parser.add_argument('--max_images', type=int, default=10,
                       help='Maximum number of images to process')
    
    args = parser.parse_args()
    
    # Set default paths if not provided
    if len(os.sys.argv) == 1 or not args.input_dir:
        # Default configuration
        base_path = "/home/alekseibuzovkin/ffhq/00000/"
        results_base = "/home/alekseibuzovkin/ffhq/fal_results/"
        prompts_json = "prompts_maximal_fal.json"
        max_concurrent = 3
        max_images = 50
    else:
        base_path = args.input_dir
        results_base = args.output_dir
        prompts_json = args.prompts_json
        max_concurrent = args.max_concurrent
        max_images = args.max_images
    
    print("FAL.ai Benchmark Image Generation")
    print("=" * 50)
    print(f"Input directory: {base_path}")
    print(f"Output directory: {results_base}")
    print(f"Prompts JSON: {prompts_json}")
    print(f"Max concurrent: {max_concurrent}")
    print(f"Max images: {max_images}")
    
    # Load prompts from JSON
    if not os.path.exists(prompts_json):
        print(f"Error: Prompts JSON file not found: {prompts_json}")
        return
    
    organized_prompts, config = load_prompts_from_json(prompts_json)
    
    print(f"\nLoaded prompts from JSON:")
    for category, data in organized_prompts.items():
        print(f"  {category}: {len(data['prompts'])} prompts")
    
    # Create main results directory
    os.makedirs(results_base, exist_ok=True)
    
    # Get list of images
    if not os.path.exists(base_path):
        print(f"Error: Input directory not found: {base_path}")
        return
        
    image_files = [f for f in os.listdir(base_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files = sorted(image_files)[:max_images]
    
    print(f"Found {len(image_files)} images to process")
    
    # Create list of all tasks
    tasks = []
    for img_file in image_files:
        img_path = os.path.join(base_path, img_file)
        img_name = os.path.splitext(img_file)[0]
        
        for category, category_data in organized_prompts.items():
            prompts = category_data['prompts']
            metadata = category_data['metadata']
            
            for prompt_idx, (prompt, prompt_meta) in enumerate(zip(prompts, metadata)):
                # Create output filename following benchmark naming convention:
                # original_name_category_intensity_promptid.png
                intensity_short = prompt_meta['intensity'].split('_')[1]  # Extract 'subtle', 'moderate', 'intense'
                prompt_id = prompt_meta['id']
                
                output_filename = f"{img_name}_{category}_{intensity_short}_{prompt_id}.png"
                output_path = os.path.join(results_base, output_filename)
                
                # Only add task if output doesn't exist
                if not os.path.exists(output_path):
                    tasks.append((
                        img_file, 
                        img_path, 
                        category, 
                        prompt_idx, 
                        prompt, 
                        output_path,
                        prompt_id
                    ))
    
    total_tasks = len(tasks)
    print(f"Total tasks to process: {total_tasks}")
    
    if total_tasks == 0:
        print("All images already processed!")
        return
    
    # Show some example tasks
    print("\nExample tasks:")
    for i, task in enumerate(tasks[:3]):
        img_file, _, category, prompt_idx, prompt, output_path, prompt_id = task
        print(f"  {i+1}. {img_file} -> {os.path.basename(output_path)}")
        print(f"     Prompt {prompt_id}: {prompt[:80]}...")
    
    if total_tasks > 3:
        print(f"  ... and {total_tasks - 3} more tasks")
    
    # Process tasks with controlled concurrency
    print(f"\nStarting processing with max {max_concurrent} concurrent requests...")
    
    await process_batch_with_semaphore(tasks, max_concurrent)
    
    # Final statistics
    completed, failed = get_counts()
    print(f"\nProcessing complete!")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    if completed + failed > 0:
        print(f"Success rate: {completed/(completed+failed)*100:.1f}%")
    
    if failed > 0:
        print(f"Check 'failed_generations_fal_benchmark.log' for failed tasks")
    
    # Summary of generated files
    print(f"\nGenerated images saved to: {results_base}")
    if os.path.exists(results_base):
        file_count = len([f for f in os.listdir(results_base) if f.endswith('.png')])
        print(f"Total generated files: {file_count}")
        
        # Show breakdown by category
        category_counts = {}
        for f in os.listdir(results_base):
            if f.endswith('.png'):
                # Extract category from filename: original_name_category_intensity_promptid.png
                parts = f.split('_')
                if len(parts) >= 4:
                    category = parts[-3]  # category is third from the end
                    category_counts[category] = category_counts.get(category, 0) + 1
        
        print("Files by category:")
        for category, count in category_counts.items():
            print(f"  {category}: {count} files")
    
    # Log benchmark completion
    summary = {
        "benchmark_info": config['benchmark_info'],
        "generation_summary": {
            "total_tasks": total_tasks,
            "completed": completed,
            "failed": failed,
            "success_rate": completed/(completed+failed)*100 if (completed+failed) > 0 else 0,
            "images_processed": len(image_files),
            "categories": list(organized_prompts.keys()),
            "output_directory": results_base,
            "api": "fal.ai",
            "model": "fal-ai/bagel/edit"
        }
    }
    
    with open(os.path.join(results_base, "fal_generation_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nGeneration summary saved to: {os.path.join(results_base, 'fal_generation_summary.json')}")

if __name__ == "__main__":
    # Make sure you have fal_client configured with your API key
    # export FAL_KEY="your-fal-api-key"
    
    print("Starting FAL.ai Bagel Edit benchmark processing...")
    print("Make sure your FAL_KEY environment variable is set!")
    
    asyncio.run(main())
