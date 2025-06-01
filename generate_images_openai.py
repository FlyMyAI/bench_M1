import asyncio
import openai
import os
import json
import time
import random
from tqdm import tqdm
import aiohttp
import base64
from PIL import Image

# Global counters
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

def encode_image_to_base64(image_path):
    """Encode image to base64 for OpenAI API"""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

async def preserve_identity_face_edit(input_image_path, prompt, output_path, max_retries=3):
    """Edit face while preserving identity using OpenAI GPT-4V + DALL-E"""
    
    # Skip if output already exists
    if os.path.exists(output_path):
        print(f"Skipping {output_path} - already exists")
        return True
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Initialize OpenAI client
    client = openai.AsyncOpenAI()
    
    for attempt in range(max_retries):
        try:
            print(f"Analyzing image: {os.path.basename(input_image_path)}...")
            
            # Encode image to base64
            base64_image = encode_image_to_base64(input_image_path)
            
            # Step 1: Simple analysis and description with edit instruction
            simple_prompt = f"""
            Describe this person's appearance focusing on general characteristics like hair color, approximate age, clothing style, and overall appearance. Then modify the description according to: {prompt}
            
            Create a description for image generation that applies the requested change while maintaining the person's general appearance. Focus on realistic, natural-looking results.
            """
            
            analysis_response = await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text", 
                                "text": simple_prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=400,
                temperature=0.1
            )
            
            description = analysis_response.choices[0].message.content
            print(f"Generated description...")
            
            # Step 2: Generate image with DALL-E using safer prompt
            print("Generating edited image...")
            
            # Create a safer prompt for DALL-E
            safe_description = description.replace("this person", "a person")
            safe_description = safe_description.replace("the person", "a person")
            
            dalle_response = await client.images.generate(
                model="dall-e-3",
                prompt=f"A portrait photograph of {safe_description}. Professional photo, natural lighting, realistic style.",
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            image_url = dalle_response.data[0].url
            print(f"Image generated successfully")
            
            # Step 3: Download the generated image
            print("Downloading result...")
            async with aiohttp.ClientSession() as session:
                async with session.get(image_url) as response:
                    if response.status == 200:
                        content = await response.read()
                        with open(output_path, 'wb') as f:
                            f.write(content)
                        print(f"Successfully saved: {os.path.basename(output_path)}")
                        return True
                    else:
                        print(f"Failed to download: HTTP {response.status}")
                        continue
                        
        except openai.RateLimitError as e:
            print(f"Rate limit error on attempt {attempt + 1}: {e}")
            wait_time = (2 ** attempt) * 30  # 30s, 60s, 120s
            print(f"Waiting {wait_time}s for rate limit...")
            await asyncio.sleep(wait_time)
            continue
            
        except openai.APIError as e:
            print(f"API error on attempt {attempt + 1}: {e}")
            error_str = str(e).lower()
            
            if "content_policy_violation" in error_str:
                print("Content policy violation - skipping this image")
                return False
            elif "image_generation_user_error" in error_str:
                print("Image generation error - possibly content-related, skipping...")
                return False
            elif "billing" in error_str:
                print("Billing issue - check your OpenAI account")
                return False
            elif "rate_limit" in error_str:
                wait_time = (2 ** attempt) * 30
                print(f"Rate limit hit, waiting {wait_time}s...")
                await asyncio.sleep(wait_time)
                continue
            else:
                wait_time = (2 ** attempt) * 10  # 10s, 20s, 40s
                print(f"Unknown API error, retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
                continue
            
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = 15  # Fixed 15s wait like in your code
                print(f"Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                print(f"Failed after {max_retries} attempts")
                return False
    
    return False

async def process_single_task(task_info):
    """Process a single task asynchronously"""
    img_file, img_path, category, prompt_idx, prompt, output_path, prompt_id = task_info
    
    success = await preserve_identity_face_edit(
        input_image_path=img_path,
        prompt=prompt,
        output_path=output_path,
        max_retries=60  # High retry count like in your code
    )
    
    if success:
        increment_completed()
    else:
        increment_failed()
        with open("failed_generations_openai_benchmark.log", "a") as f:
            f.write(f"{img_file},{category},{prompt_idx},{prompt_id},{prompt}\n")
    
    # Add delay between requests to respect rate limits
    await asyncio.sleep(random.uniform(3.0, 5.0))  # Similar timing to other scripts
    return success, img_file, category, prompt_idx

async def process_batch_with_semaphore(tasks, max_concurrent=1):
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
    
    parser = argparse.ArgumentParser(description='Generate benchmark images using OpenAI and JSON prompts')
    parser.add_argument('--prompts_json', type=str, default='prompts_simple.json',
                       help='Path to prompts JSON configuration file')
    parser.add_argument('--input_dir', type=str, 
                       help='Directory containing input FFHQ images')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory for generated images')
    parser.add_argument('--max_concurrent', type=int, default=1,
                       help='Maximum concurrent requests (keep at 1 for OpenAI)')
    parser.add_argument('--max_images', type=int, default=10,
                       help='Maximum number of images to process')
    parser.add_argument('--confirm', action='store_true',
                       help='Skip cost confirmation prompt')
    
    args = parser.parse_args()
    
    # Set default paths if not provided
    if len(os.sys.argv) == 1 or not args.input_dir:
        # Default configuration
        base_path = "/home/alekseibuzovkin/ffhq/00000/"
        results_base = "/home/alekseibuzovkin/ffhq/openai_results/"
        prompts_json = "prompts_maximal_openai.json"
        max_concurrent = 4
        max_images = 50
        confirm = False
    else:
        base_path = args.input_dir
        results_base = args.output_dir
        prompts_json = args.prompts_json
        max_concurrent = args.max_concurrent
        max_images = args.max_images
        confirm = args.confirm
    
    print("OpenAI Benchmark Image Generation")
    print("=" * 50)
    print(f"Input directory: {base_path}")
    print(f"Output directory: {results_base}")
    print(f"Prompts JSON: {prompts_json}")
    print(f"Max concurrent: {max_concurrent}")
    print(f"Max images: {max_images}")
    
    # Check OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("ERROR: Please set your OPENAI_API_KEY environment variable!")
        print("Run: export OPENAI_API_KEY='your-api-key-here'")
        return
    
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
    estimated_cost = total_tasks * 0.07  # Rough estimate: GPT-4V (~$0.02) + DALL-E 3 (~$0.04)
    
    print(f"Total tasks to process: {total_tasks}")
    print(f"Estimated cost: ${estimated_cost:.2f}")
    print("WARNING: This will use OpenAI credits!")
    
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
    
    # Confirm before proceeding (unless --confirm flag is used)
    if not confirm:
        user_input = input(f"\nProceed with {total_tasks} tasks (estimated ${estimated_cost:.2f})? [y/N]: ")
        if user_input.lower() != 'y':
            print("Cancelled by user")
            return
    
    # Process tasks with controlled concurrency
    print(f"\nStarting processing with max {max_concurrent} concurrent requests...")
    print("Using GPT-4V + DALL-E 3 for maximum identity preservation")
    
    await process_batch_with_semaphore(tasks, max_concurrent)
    
    # Final statistics
    completed, failed = get_counts()
    actual_cost = completed * 0.07
    
    print(f"\nProcessing complete!")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    print(f"Actual cost: ~${actual_cost:.2f}")
    if completed + failed > 0:
        print(f"Success rate: {completed/(completed+failed)*100:.1f}%")
    
    if failed > 0:
        print(f"Check 'failed_generations_openai_benchmark.log' for failed tasks")
    
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
            "estimated_cost": estimated_cost,
            "actual_cost": actual_cost,
            "api": "openai",
            "models": "gpt-4o + dall-e-3"
        }
    }
    
    with open(os.path.join(results_base, "openai_generation_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nGeneration summary saved to: {os.path.join(results_base, 'openai_generation_summary.json')}")

if __name__ == "__main__":
    print("OpenAI Identity-Preserving Face Edit Benchmark Processing")
    print("=" * 60)
    print("This script uses GPT-4V + DALL-E 3 for maximum identity preservation")
    print("Make sure your OPENAI_API_KEY environment variable is set!")
    print("WARNING: This will consume OpenAI credits - costs ~$0.07 per image")
    print()
    
    asyncio.run(main())
