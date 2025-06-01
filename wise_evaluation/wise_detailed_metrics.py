#!/usr/bin/env python3
"""
Detailed WISE metrics table with subcategory breakdown
"""

import json
import pandas as pd
from collections import defaultdict

def load_results():
    """Load evaluation results"""
    with open('wise_evaluation_results/evaluation_results.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_detailed_metrics_table():
    """Create detailed metrics table"""
    results = load_results()
    
    # Group by categories and subcategories
    category_data = defaultdict(lambda: defaultdict(list))
    
    for result in results['individual_results']:
        category = result['category']
        subcategory = result['subcategory']
        wiscore = result['wiscore']
        consistency = result['scores']['consistency']
        realism = result['scores']['realism']
        aesthetic = result['scores']['aesthetic_quality']
        
        category_data[category][subcategory].append({
            'wiscore': wiscore,
            'consistency': consistency,
            'realism': realism,
            'aesthetic': aesthetic
        })
    
    # Create table
    table_data = []
    
    for category, subcategories in category_data.items():
        category_wiscores = []
        category_consistency = []
        category_realism = []
        category_aesthetic = []
        
        for subcategory, scores in subcategories.items():
            sub_wiscores = [s['wiscore'] for s in scores]
            sub_consistency = [s['consistency'] for s in scores]
            sub_realism = [s['realism'] for s in scores]
            sub_aesthetic = [s['aesthetic'] for s in scores]
            
            # Add subcategory data
            table_data.append({
                'Category': category,
                'Subcategory': subcategory,
                'Count': len(scores),
                'WiScore': round(sum(sub_wiscores) / len(sub_wiscores), 3),
                'Consistency': round(sum(sub_consistency) / len(sub_consistency), 3),
                'Realism': round(sum(sub_realism) / len(sub_realism), 3),
                'Aesthetic': round(sum(sub_aesthetic) / len(sub_aesthetic), 3),
                'Type': 'Subcategory'
            })
            
            # Collect data for category totals
            category_wiscores.extend(sub_wiscores)
            category_consistency.extend(sub_consistency)
            category_realism.extend(sub_realism)
            category_aesthetic.extend(sub_aesthetic)
        
        # Add category totals
        table_data.append({
            'Category': category,
            'Subcategory': '--- TOTAL ---',
            'Count': len(category_wiscores),
            'WiScore': round(sum(category_wiscores) / len(category_wiscores), 3),
            'Consistency': round(sum(category_consistency) / len(category_consistency), 3),
            'Realism': round(sum(category_realism) / len(category_realism), 3),
            'Aesthetic': round(sum(category_aesthetic) / len(category_aesthetic), 3),
            'Type': 'Category'
        })
        
        # Add separator
        table_data.append({
            'Category': '',
            'Subcategory': '',
            'Count': '',
            'WiScore': '',
            'Consistency': '',
            'Realism': '',
            'Aesthetic': '',
            'Type': 'Separator'
        })
    
    # Overall total
    all_results = results['individual_results']
    total_wiscore = sum(r['wiscore'] for r in all_results) / len(all_results)
    total_consistency = sum(r['scores']['consistency'] for r in all_results) / len(all_results)
    total_realism = sum(r['scores']['realism'] for r in all_results) / len(all_results)
    total_aesthetic = sum(r['scores']['aesthetic_quality'] for r in all_results) / len(all_results)
    
    table_data.append({
        'Category': 'OVERALL TOTAL',
        'Subcategory': 'FlyMy AI Bot',
        'Count': len(all_results),
        'WiScore': round(total_wiscore, 3),
        'Consistency': round(total_consistency, 3),
        'Realism': round(total_realism, 3),
        'Aesthetic': round(total_aesthetic, 3),
        'Type': 'Total'
    })
    
    return pd.DataFrame(table_data)

def print_detailed_table():
    """Print detailed table"""
    df = create_detailed_metrics_table()
    
    print("=" * 120)
    print("DETAILED WISE METRICS TABLE - FlyMy AI Bot")
    print("=" * 120)
    
    # Configure pandas display
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 20)
    
    print(df.to_string(index=False))
    
    print("\n" + "=" * 120)
    print("NOTES:")
    print("   • WiScore: (0.7 × Consistency + 0.2 × Realism + 0.1 × Aesthetic) / 2")
    print("   • Consistency: Prompt adherence (0-2)")
    print("   • Realism: Image realism (0-2)")
    print("   • Aesthetic: Aesthetic quality (0-2)")
    print("=" * 120)
    
    # Save to CSV
    df.to_csv('wise_evaluation_results/detailed_metrics.csv', index=False, encoding='utf-8')
    print(f"\nTable saved to: wise_evaluation_results/detailed_metrics.csv")

if __name__ == "__main__":
    print_detailed_table() 