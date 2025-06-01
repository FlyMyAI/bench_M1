#!/usr/bin/env python3
"""
Quick progress check for WISE evaluation
"""

import json
import os
from pathlib import Path

def main():
    print("🔍 WISE Evaluation Progress Check")
    print("=" * 50)
    
    # Check results file
    results_file = Path("wise_evaluation_results/evaluation_results.json")
    if results_file.exists():
        with open(results_file, 'r') as f:
            data = json.load(f)
        
        total = data.get('total_samples', 0)
        successful = data.get('successful_evaluations', 0) 
        failed = data.get('failed_evaluations', 0)
        results = data.get('individual_results', [])
        
        print(f"📊 Current Results:")
        print(f"   Total evaluated: {successful}")
        print(f"   Failed: {failed}")
        
        if results:
            # Calculate current metrics
            total_wiscore = sum(r['wiscore'] for r in results)
            avg_wiscore = total_wiscore / len(results)
            
            avg_consistency = sum(r['scores']['consistency'] for r in results) / len(results)
            avg_realism = sum(r['scores']['realism'] for r in results) / len(results)
            avg_aesthetic = sum(r['scores']['aesthetic_quality'] for r in results) / len(results)
            
            print(f"\n📈 Current Metrics:")
            print(f"   Average WiScore: {avg_wiscore:.3f}")
            print(f"   Average Consistency: {avg_consistency:.3f}")
            print(f"   Average Realism: {avg_realism:.3f}")
            print(f"   Average Aesthetic: {avg_aesthetic:.3f}")
            
            # Category breakdown
            category_scores = {}
            for result in results:
                cat = result['category']
                if cat not in category_scores:
                    category_scores[cat] = []
                category_scores[cat].append(result['wiscore'])
            
            if category_scores:
                print(f"\n🏷️  By Category:")
                for cat, scores in category_scores.items():
                    avg_score = sum(scores) / len(scores)
                    print(f"   {cat}: {avg_score:.3f} ({len(scores)} samples)")
        
    else:
        print("❌ No results file found yet")
    
    # Check generated images
    images_dir = Path("wise_evaluation_results/images")
    if images_dir.exists():
        image_count = len(list(images_dir.glob("*.png")))
        print(f"\n🖼️  Generated Images: {image_count}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main() 