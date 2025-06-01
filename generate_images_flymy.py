import os
import requests
import json
from tqdm import tqdm
import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
load_dotenv()

# Replace with your actual API base URL
BASE_URL = "https://api.chat.flymy.ai"

# API Key
API_KEY = "REMOVED_API_KEY"

# Endpoint
endpoint = "/chat"
url = BASE_URL + endpoint

# Create session with retry strategy
def create_session():
    session = requests.Session()
    # Simplified approach - just use basic session without complex retry strategy
    session.timeout = 30
    return session

# Thread-safe counters
completed_count = 0
failed_count = 0
counter_lock = threading.Lock()

def increment_completed():
    global completed_count
    with counter_lock:
        completed_count += 1

def increment_failed():
    global failed_count
    with counter_lock:
        failed_count += 1

def get_counts():
    with counter_lock:
        return completed_count, failed_count

# Headers
headers = {
    "X-API-KEY": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

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

def process_single_task(task_info):
    """Process a single image generation task"""
    img_file, img_path, category, prompt_idx, prompt, output_path, prompt_id = task_info
    
    # Add thread ID to output for debugging
    thread_id = threading.current_thread().ident
    
    if os.path.exists(output_path):
        success = True
    else:
        success = generate_image(
            prompt=prompt,
            output_path=output_path,
            input_img_path=img_path,
            max_retries=15,
            max_wait_time=600,  # Increased timeout for longer inference
            thread_id=thread_id
        )
    
    if success:
        increment_completed()
    else:
        increment_failed()
        # Thread-safe logging
        with threading.Lock():
            with open("failed_generations.log", "a") as f:
                f.write(f"{img_file},{category},{prompt_idx},{prompt_id},{prompt}\n")
    
    # Add delay between requests (API needs time between requests)
    time.sleep(random.uniform(2.0, 3.0))  # Longer delay for sequential processing
    
    return success, img_file, category, prompt_idx

def generate_image(prompt, output_path, input_img_path=None, max_retries=15, max_wait_time=600, thread_id=None):
    """Generate image with improved error handling and retries"""
    
    thread_info = f"[Thread {thread_id}] " if thread_id else ""
    
    # Skip if output already exists
    if os.path.exists(output_path):
        print(f"{thread_info}Skipping {output_path} - already exists")
        return True
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    for attempt in range(max_retries):
        try:
            session = create_session()
            image_url = None
            
            # Upload image if provided
            if input_img_path is not None:
                print(f"{thread_info}Uploading image: {os.path.basename(input_img_path)}")
                with open(input_img_path, 'rb') as f:
                    files_payload = {'file': f}
                    headers_upload = {
                        "X-API-KEY": API_KEY,
                        "Accept": "application/json"
                    }
                    
                    upload_response = session.post(
                        BASE_URL + "/upload-image", 
                        files=files_payload, 
                        headers=headers_upload,
                        timeout=30
                    )
                    upload_response.raise_for_status()
                    image_url = BASE_URL + upload_response.json()['url']
                    print(f"{thread_info}Image uploaded successfully")

            # Prepare request body
            if image_url is not None:
                request_body = {
                    "chat_history": [
                        {
                            "role": "user",
                            "content": f"Edit image with prompt: {prompt}"
                        },
                    ],
                    "image_url": image_url
                }
            else:
                request_body = {
                    "chat_history": [
                        {
                            "role": "user",
                            "content": f"Generate image with prompt: {prompt}"
                        },
                    ],
                }

            # Send generation request
            print(f"{thread_info}Sending generation request...")
            response = session.post(url, headers=headers, json=request_body, timeout=30)
            response.raise_for_status()
            request_id = response.json()['request_id']
            print(f"{thread_info}Request ID: {request_id}")

            # Poll for result with timeout - wait longer before first check since inference takes 30-60s
            api_url_result = f"{BASE_URL}/chat-result/{request_id}"
            start_time = time.time()
            
            # Wait 15 seconds before first check (decreased from 30s)
            print(f"{thread_info}Waiting 15s before checking result (inference time)...")
            time.sleep(15)
            
            while time.time() - start_time < max_wait_time:
                try:
                    elapsed = int(time.time() - start_time)
                    print(f"{thread_info}Checking result... (elapsed: {elapsed}s)")
                    response_image = session.get(api_url_result, headers=headers, timeout=15)
                    
                    # Debug: print status code and response
                    print(f"{thread_info}Response status: {response_image.status_code}")
                    
                    if response_image.status_code == 500:
                        print(f"{thread_info}500 error - server may still be processing. Waiting longer...")
                        time.sleep(10)  # Wait 1 minute for 500 errors
                        continue
                    
                    response_image.raise_for_status()
                    result = response_image.json()
                    
                    print(f"{thread_info}Result: {result}")
                    
                    if result.get('error') != 'Still processing':
                        if result.get('success') and result.get('data') and result['data'].get('file_url'):
                            # Download the generated image
                            file_url = result['data']['file_url']
                            # Check if URL is already complete or needs BASE_URL prepended
                            if file_url.startswith('http'):
                                img_url = file_url
                            else:
                                img_url = BASE_URL + file_url
                            
                            img_response = session.get(img_url, timeout=30)
                            img_response.raise_for_status()
                            
                            with open(output_path, 'wb') as handler:
                                handler.write(img_response.content)
                            
                            print(f"{thread_info}Successfully saved: {os.path.basename(output_path)}")
                            return True
                        else:
                            print(f"{thread_info}Error in result: {result}")
                            break
                    
                    # Wait before next poll - since inference takes 30-60s, check less frequently
                    time.sleep(30 + random.uniform(0, 10))  # Wait 30-40 seconds between polls
                    
                except requests.exceptions.RequestException as e:
                    print(f"{thread_info}Error checking result: {e}")
                    # Handle 500 errors with longer backoff
                    if "500" in str(e):
                        print(f"{thread_info}Server error detected, waiting 2 minutes...")
                        time.sleep(120)  # Wait 2 minutes for server errors
                    else:
                        time.sleep(30)
                    continue
            
            print(f"{thread_info}Timeout waiting for result after {max_wait_time}s")
            
        except requests.exceptions.SSLError as e:
            print(f"{thread_info}SSL Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"{thread_info}Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"{thread_info}Failed after {max_retries} attempts due to SSL errors")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"{thread_info}Request Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"{thread_info}Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"{thread_info}Failed after {max_retries} attempts due to request errors")
                return False
                
        except Exception as e:
            print(f"{thread_info}Unexpected error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt) + random.uniform(0, 1)
                print(f"{thread_info}Retrying in {wait_time:.1f}s...")
                time.sleep(wait_time)
            else:
                print(f"{thread_info}Failed after {max_retries} attempts due to unexpected errors")
                return False
    
    return False

def main():
    """Main function to generate benchmark images using JSON prompts"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate benchmark images using JSON prompts')
    parser.add_argument('--prompts_json', type=str, default='prompts_simple.json',
                       help='Path to prompts JSON configuration file')
    parser.add_argument('--input_dir', type=str, 
                       help='Directory containing input FFHQ images')
    parser.add_argument('--output_dir', type=str,
                       help='Output directory for generated images')
    parser.add_argument('--max_workers', type=int, default=4,
                       help='Number of worker threads')
    parser.add_argument('--max_images', type=int, default=10,
                       help='Maximum number of images to process')
    
    args = parser.parse_args()
    
    # Set default paths if not provided
    if len(os.sys.argv) == 1 or not args.input_dir:
        # Default configuration
        base_path = "/home/alekseibuzovkin/ffhq/00000/"
        results_base = "/home/alekseibuzovkin/ffhq/results"
        prompts_json = "prompts_maximal_flymy.json"
        max_workers = 4
        max_images = 50
    else:
        base_path = args.input_dir
        results_base = args.output_dir
        prompts_json = args.prompts_json
        max_workers = args.max_workers
        max_images = args.max_images
    
    print("Benchmark Image Generation")
    print("=" * 50)
    print(f"Input directory: {base_path}")
    print(f"Output directory: {results_base}")
    print(f"Prompts JSON: {prompts_json}")
    print(f"Max workers: {max_workers}")
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
    
    # Process tasks with specified number of workers
    print(f"\nStarting processing with {max_workers} workers...")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_task = {executor.submit(process_single_task, task): task for task in tasks}
        
        # Process completed tasks with progress bar
        with tqdm(total=total_tasks, desc="Processing images") as pbar:
            for future in as_completed(future_to_task):
                task = future_to_task[future]
                img_file, _, category, prompt_idx, _, _, prompt_id = task
                
                try:
                    success, img_name, cat, p_idx = future.result()
                    completed, failed = get_counts()
                    
                    pbar.set_description(f"Processed {img_name} - {cat} prompt {prompt_id}")
                    pbar.set_postfix(completed=completed, failed=failed, threads=max_workers)
                    pbar.update(1)
                    
                except Exception as exc:
                    print(f"Task {task[0]} generated an exception: {exc}")
                    increment_failed()
                    pbar.update(1)
    
    # Final statistics
    completed, failed = get_counts()
    print(f"\nProcessing complete!")
    print(f"Completed: {completed}")
    print(f"Failed: {failed}")
    if completed + failed > 0:
        print(f"Success rate: {completed/(completed+failed)*100:.1f}%")
    print(f"Used {max_workers} threads for parallel processing")
    
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
            "output_directory": results_base
        }
    }
    
    with open(os.path.join(results_base, "generation_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nGeneration summary saved to: {os.path.join(results_base, 'generation_summary.json')}")

if __name__ == "__main__":
    main()
