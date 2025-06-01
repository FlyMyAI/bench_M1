#!/usr/bin/env python3

import json
import argparse
from datetime import datetime
from collections import defaultdict, Counter
import pandas as pd
import os

def load_results(results_file):
    """Load results from JSONL file"""
    results = []
    with open(results_file, 'r') as f:
        for line in f:
            results.append(json.loads(line.strip()))
    return results

def analyze_results(results):
    """Analyze results and compute detailed statistics"""
    stats = {
        'total_images': len(results),
        'total_prompts': len(set(r['prompt'] for r in results)),
        'correct_images': sum(1 for r in results if r['correct']),
        'correct_prompts': 0,
        'by_tag': defaultdict(lambda: {'total': 0, 'correct': 0, 'prompts': set()}),
        'error_analysis': defaultdict(int),
        'prompt_success': defaultdict(list)
    }
    
    # Analyze by tag and prompts
    for result in results:
        tag = result['tag']
        prompt = result['prompt']
        correct = result['correct']
        
        stats['by_tag'][tag]['total'] += 1
        stats['by_tag'][tag]['prompts'].add(prompt)
        if correct:
            stats['by_tag'][tag]['correct'] += 1
        else:
            stats['error_analysis'][result['reason']] += 1
            
        stats['prompt_success'][prompt].append(correct)
    
    # Calculate prompt-level accuracy
    stats['correct_prompts'] = sum(1 for prompt_results in stats['prompt_success'].values() 
                                  if all(prompt_results))
    
    return stats

def get_tag_description(tag):
    """Get human-readable description for each tag"""
    descriptions = {
        'single_object': 'Single object generation',
        'two_object': 'Two objects generation',
        'counting': 'Object counting accuracy (2-4 items)',
        'colors': 'Object color specification',
        'position': 'Spatial positioning of objects',
        'action': 'Actions and movements',
        'attribute': 'Additional object attributes'
    }
    return descriptions.get(tag, tag)

def generate_csv_report(results_file, output_dir, model_name="Flymy API"):
    """Generate CSV reports for detailed analysis"""
    results = load_results(results_file)
    stats = analyze_results(results)
    
    # Category summary CSV
    category_data = []
    for tag, tag_data in stats['by_tag'].items():
        accuracy = (tag_data['correct'] / tag_data['total']) * 100 if tag_data['total'] > 0 else 0
        category_data.append({
            'category': tag,
            'description': get_tag_description(tag),
            'total_images': tag_data['total'],
            'correct_images': tag_data['correct'],
            'accuracy_percent': round(accuracy, 2),
            'unique_prompts': len(tag_data['prompts']),
            'images_per_prompt': tag_data['total'] // len(tag_data['prompts']) if tag_data['prompts'] else 0
        })
    
    category_df = pd.DataFrame(category_data)
    category_df = category_df.sort_values('accuracy_percent')
    category_csv = os.path.join(output_dir, 'geneval_categories.csv')
    category_df.to_csv(category_csv, index=False)
    
    # Prompt-level CSV
    prompt_data = []
    for prompt, results_list in stats['prompt_success'].items():
        success_rate = sum(results_list) / len(results_list)
        # Find category for this prompt
        category = None
        for result in results:
            if result['prompt'] == prompt:
                category = result['tag']
                break
        
        prompt_data.append({
            'prompt': prompt,
            'category': category,
            'total_images': len(results_list),
            'correct_images': sum(results_list),
            'success_rate': round(success_rate, 4),
            'success_percent': round(success_rate * 100, 2)
        })
    
    prompt_df = pd.DataFrame(prompt_data)
    prompt_df = prompt_df.sort_values('success_rate')
    prompt_csv = os.path.join(output_dir, 'geneval_prompts.csv')
    prompt_df.to_csv(prompt_csv, index=False)
    
    # Error analysis CSV
    if stats['error_analysis']:
        error_data = []
        for error, count in stats['error_analysis'].items():
            if error.strip():
                error_data.append({
                    'error_type': error,
                    'count': count,
                    'percentage': round((count / stats['total_images']) * 100, 2)
                })
        
        error_df = pd.DataFrame(error_data)
        error_df = error_df.sort_values('count', ascending=False)
        error_csv = os.path.join(output_dir, 'geneval_errors.csv')
        error_df.to_csv(error_csv, index=False)
        
        print(f"Generated error analysis: {error_csv}")
    
    # Summary stats CSV
    image_accuracy = (stats['correct_images'] / stats['total_images']) * 100
    prompt_accuracy = (stats['correct_prompts'] / stats['total_prompts']) * 100
    
    category_scores = []
    for tag_data in stats['by_tag'].values():
        if tag_data['total'] > 0:
            category_scores.append(tag_data['correct'] / tag_data['total'])
    overall_score = sum(category_scores) / len(category_scores) if category_scores else 0
    
    summary_data = [{
        'model_name': model_name,
        'evaluation_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_images': stats['total_images'],
        'total_prompts': stats['total_prompts'],
        'correct_images': stats['correct_images'],
        'correct_prompts': stats['correct_prompts'],
        'image_accuracy_percent': round(image_accuracy, 2),
        'prompt_accuracy_percent': round(prompt_accuracy, 2),
        'overall_score': round(overall_score, 4),
        'categories_tested': len(stats['by_tag'])
    }]
    
    summary_df = pd.DataFrame(summary_data)
    summary_csv = os.path.join(output_dir, 'geneval_summary.csv')
    summary_df.to_csv(summary_csv, index=False)
    
    print(f"Generated CSV reports:")
    print(f"  - Categories: {category_csv}")
    print(f"  - Prompts: {prompt_csv}")
    print(f"  - Summary: {summary_csv}")
    
    return category_csv, prompt_csv, summary_csv

def generate_report(results_file, output_file, model_name="Flymy API"):
    """Generate detailed markdown report"""
    results = load_results(results_file)
    stats = analyze_results(results)
    
    # Generate report content
    report = []
    
    # Header
    report.append(f"# GenEval Evaluation Report")
    report.append(f"")
    report.append(f"**Model:** {model_name}")
    report.append(f"**Evaluation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Data Source:** `{results_file}`")
    report.append(f"")
    
    # Executive Summary
    image_accuracy = (stats['correct_images'] / stats['total_images']) * 100
    prompt_accuracy = (stats['correct_prompts'] / stats['total_prompts']) * 100
    
    report.append(f"## Summary Results")
    report.append(f"")
    report.append(f"| Metric | Value |")
    report.append(f"|--------|--------|")
    report.append(f"| **Overall Image Accuracy** | {image_accuracy:.2f}% ({stats['correct_images']}/{stats['total_images']}) |")
    report.append(f"| **Prompt Accuracy** | {prompt_accuracy:.2f}% ({stats['correct_prompts']}/{stats['total_prompts']}) |")
    report.append(f"| **Total Categories** | {len(stats['by_tag'])} |")
    
    # Calculate overall score (average over categories)
    category_scores = []
    for tag_data in stats['by_tag'].values():
        if tag_data['total'] > 0:
            category_scores.append(tag_data['correct'] / tag_data['total'])
    overall_score = sum(category_scores) / len(category_scores) if category_scores else 0
    
    report.append(f"| **Overall Score** | {overall_score:.4f} |")
    report.append(f"")
    
    # Performance indicator
    if overall_score >= 0.9:
        performance = "Excellent"
    elif overall_score >= 0.7:
        performance = "Good"
    elif overall_score >= 0.5:
        performance = "Satisfactory"
    else:
        performance = "Needs Improvement"
    
    report.append(f"**Overall Performance Rating:** {performance}")
    report.append(f"")
    
    # Detailed breakdown by category
    report.append(f"## Category Breakdown")
    report.append(f"")
    
    # Sort by accuracy (worst first for analysis)
    sorted_tags = sorted(stats['by_tag'].items(), 
                        key=lambda x: x[1]['correct']/x[1]['total'] if x[1]['total'] > 0 else 0)
    
    for tag, tag_data in sorted_tags:
        accuracy = (tag_data['correct'] / tag_data['total']) * 100 if tag_data['total'] > 0 else 0
        description = get_tag_description(tag)
        
        report.append(f"### {tag.upper()}: {description}")
        report.append(f"")
        report.append(f"- **Accuracy:** {accuracy:.2f}% ({tag_data['correct']}/{tag_data['total']})")
        report.append(f"- **Prompts:** {len(tag_data['prompts'])}")
        report.append(f"- **Images per Prompt:** {tag_data['total'] // len(tag_data['prompts']) if tag_data['prompts'] else 0}")
        
        # Sample prompts for this category
        sample_prompts = list(tag_data['prompts'])[:3]
        if sample_prompts:
            report.append(f"- **Example Prompts:**")
            for prompt in sample_prompts:
                report.append(f"  - \"{prompt}\"")
        
        report.append(f"")
    
    # Error Analysis
    if stats['error_analysis']:
        report.append(f"## Error Analysis")
        report.append(f"")
        report.append(f"| Error Type | Count |")
        report.append(f"|------------|-------|")
        
        for error, count in sorted(stats['error_analysis'].items(), key=lambda x: x[1], reverse=True):
            if error.strip():  # Only show non-empty errors
                report.append(f"| {error} | {count} |")
        
        report.append(f"")
    
    # Per-prompt analysis
    report.append(f"## Prompt Analysis")
    report.append(f"")
    
    # Group prompts by success rate
    prompt_stats = []
    for prompt, results_list in stats['prompt_success'].items():
        success_rate = sum(results_list) / len(results_list)
        prompt_stats.append((prompt, success_rate, len(results_list), sum(results_list)))
    
    # Sort by success rate (worst first)
    prompt_stats.sort(key=lambda x: x[1])
    
    report.append(f"| Prompt | Success Rate | Images |")
    report.append(f"|--------|--------------|--------|")
    
    for prompt, success_rate, total, correct in prompt_stats:
        report.append(f"| {prompt} | {success_rate*100:.1f}% ({correct}/{total}) | {total} |")
    
    report.append(f"")
    
    # Recommendations
    report.append(f"## Recommendations")
    report.append(f"")
    
    if overall_score >= 0.9:
        report.append(f"- Model shows excellent performance on tested categories")
        report.append(f"- Recommend expanding testing to more complex categories")
        report.append(f"- Ready for production use in current categories")
    elif overall_score >= 0.7:
        report.append(f"- Model shows good performance with room for improvement")
        report.append(f"- Recommend detailed analysis of errors in weak categories")
        report.append(f"- Consider prompt optimization for problematic cases")
    else:
        report.append(f"- Model requires significant improvement")
        report.append(f"- Analyze main error sources")
        report.append(f"- Consider additional training or parameter tuning")
    
    report.append(f"")
    
    # Technical details
    report.append(f"## Technical Details")
    report.append(f"")
    report.append(f"- **Evaluation Framework:** GenEval")
    report.append(f"- **Object Detection:** mask2former_swin-s-p4-w7-224_lsj_8x2_50e_coco")
    report.append(f"- **CLIP Model:** ViT-L-14")
    report.append(f"- **Detection Threshold:** 0.3 (0.9 for counting)")
    report.append(f"- **Images per Prompt:** 4")
    report.append(f"")
    
    # Footer
    report.append(f"---")
    report.append(f"*Report generated automatically based on GenEval evaluation results*")
    
    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"Detailed report saved to: {output_file}")
    print(f"Key metrics:")
    print(f"   - Image accuracy: {image_accuracy:.2f}%")
    print(f"   - Prompt accuracy: {prompt_accuracy:.2f}%")
    print(f"   - Overall Score: {overall_score:.4f}")

def main():
    parser = argparse.ArgumentParser(description="Generate detailed GenEval report")
    parser.add_argument("results_file", help="Path to results.jsonl file")
    parser.add_argument("--output", "-o", default="geneval_report.md", help="Output markdown file")
    parser.add_argument("--model-name", default="Flymy API", help="Name of the evaluated model")
    parser.add_argument("--csv", action="store_true", help="Generate CSV reports in addition to markdown")
    parser.add_argument("--csv-only", action="store_true", help="Generate only CSV reports, skip markdown")
    
    args = parser.parse_args()
    
    if args.csv_only:
        output_dir = os.path.dirname(args.output) or "."
        generate_csv_report(args.results_file, output_dir, args.model_name)
    elif args.csv:
        generate_report(args.results_file, args.output, args.model_name)
        output_dir = os.path.dirname(args.output) or "."
        generate_csv_report(args.results_file, output_dir, args.model_name)
    else:
        generate_report(args.results_file, args.output, args.model_name)

if __name__ == "__main__":
    main() 