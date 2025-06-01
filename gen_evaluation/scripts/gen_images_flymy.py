#!/usr/bin/env python3
# Copyright 2025 Bytedance Ltd. and/or its affiliates.
# SPDX-License-Identifier: Apache-2.0

import os
import json
import argparse
import requests
import time
from pathlib import Path
import multiprocessing as mp
from PIL import Image
import io


class FlymyImageGenerator:
    def __init__(self, api_key=None):
        self.base_url = "https://api.chat.flymy.ai"
        self.api_key = api_key or "REMOVED_API_KEY"
        self.headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def generate_image(self, prompt, max_retries=3):
        """Generate a single image using flymy API"""
        endpoint = "/chat"
        url = self.base_url + endpoint
        
        request_body = {
            "chat_history": [
                {
                    "role": "user",
                    "content": f"Generate image with prompt: {prompt}"
                }
            ]
        }
        
        for attempt in range(max_retries):
            try:
                # Add delay to avoid overwhelming the API
                time.sleep(2)  # 2 second delay before each request
                
                # Submit generation request
                response = requests.post(url, headers=self.headers, json=request_body, timeout=30)
                response.raise_for_status()
                request_id = response.json()['request_id']
                
                # Poll for results with longer intervals
                api_url_result = f"{self.base_url}/chat-result/{request_id}"
                max_poll_attempts = 30  # Reduce polling attempts
                
                for poll_attempt in range(max_poll_attempts):
                    try:
                        response_image = requests.get(api_url_result, headers=self.headers, timeout=30)
                        response_image.raise_for_status()
                        result = response_image.json()
                        
                        if result.get('error') != 'Still processing':
                            if 'data' in result and 'file_url' in result['data']:
                                # Download the image
                                img_url = self.base_url + result['data']['file_url']
                                img_response = requests.get(img_url, timeout=30)
                                img_response.raise_for_status()
                                
                                # Convert to PIL Image
                                image = Image.open(io.BytesIO(img_response.content))
                                return image
                            else:
                                print(f"Error in result: {result}")
                                break
                        
                        time.sleep(20)  # Wait 20 seconds between polls (instead of 10)
                        
                    except Exception as e:
                        print(f"Error polling for result (attempt {poll_attempt + 1}): {e}")
                        time.sleep(10)  # Longer delay on errors
                
                print(f"Timeout waiting for image generation (attempt {attempt + 1})")
                
            except Exception as e:
                print(f"Error generating image (attempt {attempt + 1}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(10)  # Longer delay between retries
        
        return None


def generate_images_for_prompt(args):
    """Generate images for a single prompt with multiple samples"""
    prompt_data, output_dir, num_images, rank = args
    
    generator = FlymyImageGenerator()
    
    idx = prompt_data['idx']
    metadata = prompt_data['metadata']
    prompt = metadata['prompt']
    
    outpath = Path(output_dir) / f"{idx:0>5}"
    outpath.mkdir(parents=True, exist_ok=True)
    
    sample_path = outpath / "samples"
    sample_path.mkdir(parents=True, exist_ok=True)
    
    print(f"Worker {rank}: Processing prompt {idx}: '{prompt}'")
    
    # Check if images already exist
    existing_images = 0
    for i in range(num_images):
        if (sample_path / f"{i:05}.png").exists():
            existing_images += 1
    
    if existing_images == num_images:
        print(f"Worker {rank}: Skipping prompt {idx} - all images already exist")
        return
    
    # Save metadata
    with open(outpath / "metadata.jsonl", "w", encoding="utf-8") as fp:
        json.dump(metadata, fp)
    
    # Generate missing images
    for i in range(existing_images, num_images):
        image_path = sample_path / f"{i:05}.png"
        print(f"Worker {rank}: Generating image {i+1}/{num_images} for prompt {idx}")
        
        image = generator.generate_image(prompt)
        if image is not None:
            # Crop to content if needed
            if hasattr(image, 'getbbox') and image.getbbox():
                image = image.crop(image.getbbox())
            image.save(image_path)
            print(f"Worker {rank}: Saved {image_path}")
        else:
            print(f"Worker {rank}: Failed to generate image {i+1} for prompt {idx}")


def main():
    parser = argparse.ArgumentParser(description="Generate images using Flymy API for GenEval.")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save the generated images.")
    parser.add_argument("--metadata_file", type=str, required=True, help="JSONL file containing lines of metadata for each prompt.")
    parser.add_argument("--num_images", type=int, default=4, help="Number of images to generate per prompt")
    parser.add_argument("--num_workers", type=int, default=4, help="Number of parallel workers")
    parser.add_argument("--start_idx", type=int, default=0, help="Start index for prompts")
    parser.add_argument("--end_idx", type=int, default=None, help="End index for prompts")
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output images will be saved in {output_dir}")
    
    # Load metadata
    with open(args.metadata_file, "r", encoding="utf-8") as fp:
        metadatas = [json.loads(line) for line in fp]
    
    # Apply start/end indices
    start_idx = args.start_idx
    end_idx = args.end_idx if args.end_idx is not None else len(metadatas)
    metadatas = metadatas[start_idx:end_idx]
    
    print(f"Processing {len(metadatas)} prompts (indices {start_idx} to {end_idx-1})")
    
    # Prepare prompt data with indices
    prompt_data_list = []
    for i, metadata in enumerate(metadatas):
        prompt_data_list.append({
            'idx': start_idx + i,
            'metadata': metadata
        })
    
    # Prepare arguments for multiprocessing
    worker_args = []
    for i, prompt_data in enumerate(prompt_data_list):
        worker_args.append((prompt_data, str(output_dir), args.num_images, i % args.num_workers))
    
    # Process using multiprocessing
    with mp.Pool(processes=args.num_workers) as pool:
        pool.map(generate_images_for_prompt, worker_args)
    
    print("All image generation tasks completed!")


if __name__ == "__main__":
    main() 