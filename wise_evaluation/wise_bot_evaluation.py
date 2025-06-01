#!/usr/bin/env python3
"""
WISE evaluation for FlyMy AI Bot.
"""

import json
import os
import argparse
import random
from datetime import datetime
from pathlib import Path
import pandas as pd
from wise_utils import load_wise_dataset, evaluate_image_with_gpt4, find_processed_samples
from bot_api import FlyMyAIBot

def select_diverse_samples(wise_data, total_samples=100):
    """Select diverse samples from different categories."""
    if total_samples >= len(wise_data):
        return wise_data
    
    # Group by category
    categories = {}
    for sample in wise_data:
        cat = sample['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(sample)
    
    print(f"Available categories: {list(categories.keys())}")
    print(f"Category distribution:")
    for cat, samples in categories.items():
        print(f"   {cat}: {len(samples)} samples")
    
    # Calculate samples per category
    num_categories = len(categories)
    samples_per_category = total_samples // num_categories
    remaining_samples = total_samples % num_categories
    
    selected_samples = []
    category_names = list(categories.keys())
    
    # Select samples from each category
    for i, (cat, samples) in enumerate(categories.items()):
        extra = 1 if i < remaining_samples else 0
        target_count = samples_per_category + extra
        
        if len(samples) <= target_count:
            selected_samples.extend(samples)
        else:
            selected_samples.extend(random.sample(samples, target_count))
    
    # Shuffle final selection
    random.shuffle(selected_samples)
    
    print(f"Selected {len(selected_samples)} diverse samples")
    print(f"Final distribution:")
    final_categories = {}
    for sample in selected_samples:
        cat = sample['category']
        final_categories[cat] = final_categories.get(cat, 0) + 1
    
    for cat, count in final_categories.items():
        print(f"   {cat}: {count} samples")
    
    return selected_samples

def save_intermediate_results(results_file, all_results, failed_count, diverse_sampling):
    """Save intermediate results after each successful evaluation."""
    if all_results:
        total_wiscore = sum(r['wiscore'] for r in all_results)
        avg_wiscore = total_wiscore / len(all_results)
        
        avg_consistency = sum(r['scores']['consistency'] for r in all_results) / len(all_results)
        avg_realism = sum(r['scores']['realism'] for r in all_results) / len(all_results)
        avg_aesthetic = sum(r['scores']['aesthetic_quality'] for r in all_results) / len(all_results)
        
        # Calculate category breakdown
        category_scores = {}
        for result in all_results:
            cat = result['category']
            if cat not in category_scores:
                category_scores[cat] = []
            category_scores[cat].append(result['wiscore'])
        
        category_averages = {}
        for cat, scores in category_scores.items():
            category_averages[cat] = sum(scores) / len(scores)
        
        summary = {
            "average_wiscore": avg_wiscore,
            "average_consistency": avg_consistency,
            "average_realism": avg_realism,
            "average_aesthetic": avg_aesthetic,
            "category_scores": category_averages
        }
    else:
        summary = {}
    
    # Save results
    output_data = {
        "evaluation_date": datetime.now().isoformat(),
        "model_info": "FlyMy AI Bot (api.chat.flymy.ai)",
        "diverse_sampling": diverse_sampling,
        "total_samples": len(all_results),
        "successful_evaluations": len(all_results),
        "failed_evaluations": failed_count,
        "individual_results": all_results,
        "summary": summary
    }
    
    with open(results_file, 'w') as f:
        json.dump(output_data, f, indent=2)

def run_wise_evaluation(continue_evaluation=False, samples_limit=None, diverse_sampling=True):
    """Run WISE evaluation on FlyMy AI Bot."""
    
    print("=" * 80)
    print("WISE EVALUATION - FlyMy AI Bot")
    print("=" * 80)
    
    # Load WISE dataset
    wise_data = load_wise_dataset()
    print(f"Loaded {len(wise_data)} total samples from WISE dataset")
    
    # Setup output directories
    results_dir = Path("wise_evaluation_results")
    results_dir.mkdir(exist_ok=True)
    
    images_dir = results_dir / "images"
    results_file = results_dir / "evaluation_results.json"
    
    images_dir.mkdir(exist_ok=True)
    
    # Check for existing results if continuing
    existing_results = []
    processed_samples = set()
    
    if continue_evaluation and results_file.exists():
        with open(results_file, 'r') as f:
            data = json.load(f)
        existing_results = data.get('individual_results', [])
        processed_samples = find_processed_samples(existing_results)
        print(f"Found {len(processed_samples)} already processed samples")
        
        # Filter out processed samples
        remaining_data = [sample for sample in wise_data if sample['id'] not in processed_samples]
        remaining_count = min(len(remaining_data), (samples_limit or 100) - len(processed_samples))
        print(f"Continuing evaluation - {remaining_count} remaining samples")
        
        if diverse_sampling:
            wise_data = select_diverse_samples(remaining_data, remaining_count)
        else:
            wise_data = remaining_data[:remaining_count]
        
        if existing_results:
            print(f"Loaded {len(existing_results)} existing results")
    else:
        total_samples = samples_limit if samples_limit else 100
        print(f"Evaluating {total_samples} samples")
        
        if diverse_sampling:
            wise_data = select_diverse_samples(wise_data, total_samples)
        else:
            wise_data = wise_data[:total_samples]
    
    # Initialize bot
    bot = FlyMyAIBot()
    
    # Process samples
    results = []
    failed_count = 0
    
    for i, sample in enumerate(wise_data, 1):
        sample_id = sample['id']
        prompt = sample['prompt']
        category = sample['category']
        subcategory = sample['subcategory']
        
        print(f"--- Sample {i}/{len(wise_data)} (ID: {sample_id}) ---")
        print(f"Category: {category} / {subcategory}")
        print(f"Generating image for prompt: {prompt[:50]}...")
        
        # Generate unique filename
        timestamp = int(datetime.now().timestamp())
        image_filename = f"sample_{sample_id}_{timestamp}.png"
        image_path = images_dir / image_filename
        
        # Generate image
        success, original_prompt, final_prompt = bot.generate_image(prompt, str(image_path))
        
        if not success:
            print(f"Failed to generate image for sample {sample_id}")
            failed_count += 1
            # Save intermediate results even on failure
            all_results = existing_results + results
            save_intermediate_results(results_file, all_results, failed_count, diverse_sampling)
            continue
        
        print(f"Image saved to: {image_path}")
        
        # Evaluate with GPT-4o
        print("Evaluating image with GPT-4o...")
        try:
            scores = evaluate_image_with_gpt4(str(image_path), prompt)
            
            if not scores:
                print(f"Failed to evaluate sample {sample_id}")
                failed_count += 1
                continue
            
            # Calculate WiScore
            wiscore = (0.7 * scores['consistency'] + 0.2 * scores['realism'] + 0.1 * scores['aesthetic_quality']) / 2.0
            
            # Store result
            result = {
                "sample_id": sample_id,
                "category": category,
                "subcategory": subcategory,
                "prompt": prompt,
                "image_path": str(image_path),
                "model_used": "FlyMy AI Bot",
                "scores": scores,
                "wiscore": wiscore,
                "timestamp": datetime.now().isoformat()
            }
            
            results.append(result)
            
            # Show progress
            print(f"Prompt: {prompt[:50]}...")
            print(f"WiScore: {wiscore:.3f}")
            print(f"Scores - Consistency: {scores['consistency']}, Realism: {scores['realism']}, Aesthetic: {scores['aesthetic_quality']}")
            
            # SAVE INTERMEDIATE RESULTS after each successful evaluation
            all_results = existing_results + results
            save_intermediate_results(results_file, all_results, failed_count, diverse_sampling)
            print(f"✅ Progress saved ({len(all_results)} total samples)")
            
        except Exception as e:
            print(f"Error evaluating sample {sample_id}: {e}")
            failed_count += 1
            continue
    
    # Final save (already done incrementally, but for completeness)
    all_results = existing_results + results
    save_intermediate_results(results_file, all_results, failed_count, diverse_sampling)
    
    print(f"\nEvaluation complete!")
    print(f"Results saved to: {results_file}")
    print(f"Images saved to: {images_dir}")
    if all_results:
        avg_wiscore = sum(r['wiscore'] for r in all_results) / len(all_results)
        print(f"Average WiScore: {avg_wiscore:.3f}")

def main():
    parser = argparse.ArgumentParser(description='Run WISE evaluation on FlyMy AI Bot')
    parser.add_argument('--continue', action='store_true', help='Continue from existing results')
    parser.add_argument('--samples', type=int, help='Limit number of samples to evaluate')
    parser.add_argument('--no-diverse', action='store_true', help='Disable diverse sampling')
    
    args = parser.parse_args()
    
    run_wise_evaluation(
        continue_evaluation=getattr(args, 'continue'), 
        samples_limit=args.samples,
        diverse_sampling=not args.no_diverse
    )

if __name__ == "__main__":
    main() 