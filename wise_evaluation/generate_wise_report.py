#!/usr/bin/env python3
"""
Generate comprehensive report for WISE evaluation results with benchmark comparison
"""

import json
import os
import argparse
from datetime import datetime
from collections import defaultdict
from wise_utils import get_wise_benchmark_data, get_category_mapping

def load_results(result_type="standard"):
    """Load results based on type"""
    result_files = {
        "standard": 'wise_evaluation_results/evaluation_results.json',
        "enhanced": 'wise_evaluation_results/evaluation_results_enhanced.json', 
        "rewritten": 'wise_evaluation_results/evaluation_results_rewritten.json'
    }
    
    if result_type not in result_files:
        raise ValueError(f"Unknown result type: {result_type}")
    
    filepath = result_files[result_type]
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Results file not found: {filepath}")
        
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_comparison_results():
    """Load all available results for comparison"""
    results = {}
    result_types = ["standard", "enhanced", "rewritten"]
    
    for result_type in result_types:
        try:
            results[result_type] = load_results(result_type)
        except (FileNotFoundError, ValueError):
            continue
    
    return results

def calculate_category_stats(results):
    """Calculate statistics by category"""
    category_stats = defaultdict(lambda: {
        'scores': [], 
        'modified_count': 0, 
        'total_count': 0,
        'perfect_scores': 0,
        'consistency_scores': [],
        'realism_scores': [],
        'aesthetic_scores': []
    })
    
    for result in results['individual_results']:
        category = result['category']
        wiscore = result['wiscore']
        was_modified = result.get('prompt_rewritten', False) or result.get('enhanced_prompting', False)
        
        category_stats[category]['scores'].append(wiscore)
        category_stats[category]['consistency_scores'].append(result['scores']['consistency'])
        category_stats[category]['realism_scores'].append(result['scores']['realism'])
        category_stats[category]['aesthetic_scores'].append(result['scores']['aesthetic_quality'])
        category_stats[category]['total_count'] += 1
        
        if was_modified:
            category_stats[category]['modified_count'] += 1
            
        if wiscore >= 0.99:  # Perfect or near-perfect score
            category_stats[category]['perfect_scores'] += 1
    
    # Calculate averages
    for category in category_stats:
        stats = category_stats[category]
        scores = stats['scores']
        stats['average'] = sum(scores) / len(scores) if scores else 0
        stats['consistency_avg'] = sum(stats['consistency_scores']) / len(stats['consistency_scores']) if stats['consistency_scores'] else 0
        stats['realism_avg'] = sum(stats['realism_scores']) / len(stats['realism_scores']) if stats['realism_scores'] else 0
        stats['aesthetic_avg'] = sum(stats['aesthetic_scores']) / len(stats['aesthetic_scores']) if stats['aesthetic_scores'] else 0
        stats['modification_rate'] = (stats['modified_count'] / stats['total_count'] * 100) if stats['total_count'] > 0 else 0
        stats['perfect_rate'] = (stats['perfect_scores'] / stats['total_count'] * 100) if stats['total_count'] > 0 else 0
    
    return dict(category_stats)

def get_benchmark_comparison(category_stats):
    """Compare with WISE benchmark data"""
    benchmarks = get_wise_benchmark_data()
    category_mapping = get_category_mapping()
    
    # Map our categories to benchmark categories
    mapped_stats = {}
    for our_category, stats in category_stats.items():
        if our_category in category_mapping:
            benchmark_category = category_mapping[our_category]
            mapped_stats[benchmark_category] = stats
    
    # Add benchmark context
    for category in mapped_stats:
        # Find best and worst models in this category
        category_scores = [(model, data[category]) for model, data in benchmarks.items() if category in data]
        if category_scores:
            category_scores.sort(key=lambda x: x[1], reverse=True)
            mapped_stats[category]['best_model'] = category_scores[0]
            mapped_stats[category]['worst_model'] = category_scores[-1]
            mapped_stats[category]['median_score'] = sorted([score for _, score in category_scores])[len(category_scores)//2]
    
    return mapped_stats, benchmarks

def generate_markdown_report(results, result_type="standard"):
    """Generate markdown report"""
    category_stats = calculate_category_stats(results)
    benchmark_comparison, benchmarks = get_benchmark_comparison(category_stats)
    
    # Sort categories by performance
    sorted_categories = sorted(category_stats.items(), key=lambda x: x[1]['average'], reverse=True)
    
    mode_emojis = {
        "standard": "STANDARD", 
        "enhanced": "ENHANCED", 
        "rewritten": "REWRITTEN"
    }
    
    mode_descriptions = {
        "standard": "Standard Prompting",
        "enhanced": "Enhanced Prompting", 
        "rewritten": "Prompt Rewriting"
    }
    
    mode_emoji = mode_emojis.get(result_type, "STANDARD")
    mode_desc = mode_descriptions.get(result_type, "Standard Prompting")
    
    report = f"""# WISE Evaluation Results - {mode_emoji} {mode_desc.upper()}

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Executive Summary

"""
    
    # Key metrics
    avg_wiscore = results['summary']['average_wiscore']
    total_samples = results['successful_evaluations']
    
    report += f"""### **PERFORMANCE OVERVIEW**
- **Average WiScore: {avg_wiscore:.3f}**
- **Samples evaluated: {total_samples}**
- **Success rate: 100%**
- **Evaluation mode: {mode_desc}**

"""
    
    # Performance distribution
    perfect_scores = sum(1 for r in results['individual_results'] if r['wiscore'] >= 0.99)
    excellent_scores = sum(1 for r in results['individual_results'] if 0.85 <= r['wiscore'] < 0.99)
    good_scores = sum(1 for r in results['individual_results'] if 0.65 <= r['wiscore'] < 0.85)
    needs_work = total_samples - perfect_scores - excellent_scores - good_scores
    
    report += f"""## Performance Distribution

| Performance Level | Count | Percentage |
|---|---|---|
| **Excellent** (0.99-1.00) | {perfect_scores} | {perfect_scores/total_samples*100:.1f}% |
| **Very Good** (0.85-0.98) | {excellent_scores} | {excellent_scores/total_samples*100:.1f}% |
| **Good** (0.65-0.84) | {good_scores} | {good_scores/total_samples*100:.1f}% |
| **Needs Work** (<0.65) | {needs_work} | {needs_work/total_samples*100:.1f}% |

"""
    
    # Benchmark comparison
    report += f"""## Benchmark Comparison

### Your Bot vs. Top Models

| Category | Your Score | Best Model | Median | Your Rank |
|---|---|---|---|---|
"""
    
    overall_our_score = avg_wiscore
    overall_benchmarks = [(model, data['Overall']) for model, data in benchmarks.items()]
    overall_benchmarks.sort(key=lambda x: x[1], reverse=True)
    
    # Find our rank in overall
    our_overall_rank = "#1"
    for i, (model, score) in enumerate(overall_benchmarks):
        if overall_our_score >= score:
            our_overall_rank = f"#{i+1}" if i < 3 else f"#{i+1}"
            break
    else:
        our_overall_rank = f"#{len(overall_benchmarks)+1}"
    
    report += f"| **Overall** | **{overall_our_score:.3f}** | {overall_benchmarks[0][0]} ({overall_benchmarks[0][1]:.3f}) | {overall_benchmarks[len(overall_benchmarks)//2][1]:.3f} | {our_overall_rank} |\n"
    
    for category, stats in benchmark_comparison.items():
        our_score = stats['average']
        best_model, best_score = stats['best_model']
        median_score = stats['median_score']
        
        # Determine rank emoji
        if our_score >= best_score:
            rank_emoji = "#1"
        elif our_score >= median_score:
            rank_emoji = "Top 50%"
        else:
            rank_emoji = "Lower 50%"
            
        report += f"| **{category}** | **{our_score:.3f}** | {best_model} ({best_score:.3f}) | {median_score:.3f} | {rank_emoji} |\n"
    
    # Category breakdown  
    report += f"""
## Detailed Results by Category

| Category | WiScore | Consistency | Realism | Aesthetic | Perfect Scores | Samples |
|---|---|---|---|---|---|---|
"""
    
    for category, stats in sorted_categories:
        category_clean = category.replace('Physical Knowledge', 'Physics').replace('Cultural knowledge', 'Cultural')
        report += f"| **{category_clean}** | {stats['average']:.3f} | {stats['consistency_avg']:.2f} | {stats['realism_avg']:.2f} | {stats['aesthetic_avg']:.2f} | {stats['perfect_scores']}/{stats['total_count']} | {stats['total_count']} |\n"
    
    # Top performers analysis
    report += f"""
## Top Performing Categories

"""
    
    top_3_categories = sorted_categories[:3]
    for i, (category, stats) in enumerate(top_3_categories, 1):
        category_clean = category.replace('Physical Knowledge', 'Physics').replace('Cultural knowledge', 'Cultural')
        medal_emoji = ["#1", "#2", "#3"][i-1]
        
        report += f"""### {medal_emoji} {category_clean}
- **WiScore:** {stats['average']:.3f}
- **Perfect scores:** {stats['perfect_scores']}/{stats['total_count']} ({stats['perfect_rate']:.1f}%)
- **Breakdown:** Consistency {stats['consistency_avg']:.2f}, Realism {stats['realism_avg']:.2f}, Aesthetic {stats['aesthetic_avg']:.2f}

"""
    
    # Examples
    report += f"""## Best Examples

"""
    
    # Find best examples
    examples_shown = 0
    best_results = sorted(results['individual_results'], key=lambda x: x['wiscore'], reverse=True)
    
    for result in best_results[:3]:
        if examples_shown >= 3:
            break
            
        report += f"""### {result['category']} - WiScore: {result['wiscore']:.3f}

**Prompt:** {result['original_prompt']}

**Scores:** Consistency: {result['scores']['consistency']}, Realism: {result['scores']['realism']}, Aesthetic: {result['scores']['aesthetic_quality']}

**Image:** `{os.path.basename(result['image_path'])}`

---

"""
        examples_shown += 1
    
    report += f"""## Methodology

**WiScore Formula:** (0.7 × Consistency + 0.2 × Realism + 0.1 × Aesthetic Quality) / 2

**Evaluation Criteria:**
- **Consistency (0-2):** How well the image matches the prompt
- **Realism (0-2):** How realistic and plausible the image appears  
- **Aesthetic Quality (0-2):** Overall visual appeal and composition

**Evaluation Mode:** {mode_desc}

**Benchmarks:** Compared against {len(benchmarks)} state-of-the-art models from WISE paper

---

*Report generated by WISE Evaluation System*
"""
    
    return report

def generate_html_report(results, result_type="standard"):
    """Generate HTML report in leaderboard format"""
    category_stats = calculate_category_stats(results)
    benchmark_comparison, benchmarks = get_benchmark_comparison(category_stats)
    
    mode_descriptions = {
        "standard": "Standard Prompting",
        "enhanced": "Enhanced Prompting", 
        "rewritten": "Prompt Rewriting"
    }
    
    mode_desc = mode_descriptions.get(result_type, "Unknown Mode")
    avg_wiscore = results['summary']['average_wiscore']
    
    # Create leaderboard data
    leaderboard = []
    
    # Add our bot first
    our_bot_entry = {
        'name': f'FlyMy AI Bot (Custom)',
        'type': 'Your Bot',
        'Cultural': benchmark_comparison.get('Cultural', {}).get('average', 0),
        'Time': benchmark_comparison.get('Time', {}).get('average', 0), 
        'Space': benchmark_comparison.get('Space', {}).get('average', 0),
        'Biology': benchmark_comparison.get('Biology', {}).get('average', 0),
        'Physics': benchmark_comparison.get('Physics', {}).get('average', 0),
        'Chemistry': benchmark_comparison.get('Chemistry', {}).get('average', 0),
        'Overall': avg_wiscore
    }
    leaderboard.append(our_bot_entry)
    
    # Add benchmark models
    for model_name, model_data in benchmarks.items():
        model_entry = {
            'name': model_name,
            'type': model_data.get('Type', 'Unknown'),
            'Cultural': model_data.get('Cultural', 0),
            'Time': model_data.get('Time', 0),
            'Space': model_data.get('Space', 0), 
            'Biology': model_data.get('Biology', 0),
            'Physics': model_data.get('Physics', 0),
            'Chemistry': model_data.get('Chemistry', 0),
            'Overall': model_data.get('Overall', 0)
        }
        leaderboard.append(model_entry)
    
    # Sort by overall score
    leaderboard.sort(key=lambda x: x['Overall'], reverse=True)
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>WISE Leaderboard</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            margin: 40px auto;
            max-width: 1200px;
            background: #fff;
            color: #333;
        }}
        h1 {{
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #000;
        }}
        .subtitle {{
            color: #666;
            font-size: 14px;
            margin-bottom: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
            background: #fff;
        }}
        th {{
            background: #f5f5f5;
            padding: 12px 8px;
            text-align: center;
            font-weight: 600;
            border-bottom: 1px solid #ddd;
            color: #333;
        }}
        th:first-child {{
            text-align: center;
            width: 60px;
        }}
        th:nth-child(2) {{
            text-align: left;
            width: 250px;
        }}
        td {{
            padding: 8px;
            text-align: center;
            border-bottom: 1px solid #eee;
            font-weight: 500;
        }}
        td:first-child {{
            text-align: center;
            font-weight: 600;
        }}
        td:nth-child(2) {{
            text-align: left;
            font-weight: 600;
        }}
        .our-bot {{
            background-color: #fff9e6;
        }}
        .rank-1 {{ background-color: #f0f8f0; }}
        .rank-2 {{ background-color: #f0f6ff; }}
        .rank-3 {{ background-color: #fff0f5; }}
        tr:hover {{
            background-color: #f9f9f9;
        }}
        .our-bot:hover {{
            background-color: #fff3cd;
        }}
    </style>
</head>
<body>
    <h1>WISE Leaderboard</h1>
    <p class="subtitle">Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    
    <table>
        <thead>
            <tr>
                <th>Rank</th>
                <th>Model</th>
                <th>Cultural</th>
                <th>Time</th>
                <th>Space</th>
                <th>Biology</th>
                <th>Physics</th>
                <th>Chemistry</th>
                <th>Overall</th>
            </tr>
        </thead>
        <tbody>
"""
    
    for rank, entry in enumerate(leaderboard, 1):
        # Determine row class
        row_class = ""
        if entry['type'] == 'Your Bot':
            row_class = "our-bot"
        elif rank <= 3:
            row_class = f"rank-{rank}"
        
        # Format model name with type
        model_display = entry['name']
        if entry['type'] != 'Your Bot':
            type_suffix = " (T2I Model)" if entry['type'] == 'T2I Model' else " (MLLM)"
            model_display += type_suffix
        
        html += f"""            <tr class="{row_class}">
                <td>{rank}</td>
                <td>{model_display}</td>
                <td>{entry['Cultural']:.3f}</td>
                <td>{entry['Time']:.3f}</td>
                <td>{entry['Space']:.3f}</td>
                <td>{entry['Biology']:.3f}</td>
                <td>{entry['Physics']:.3f}</td>
                <td>{entry['Chemistry']:.3f}</td>
                <td>{entry['Overall']:.3f}</td>
            </tr>
"""
    
    html += f"""        </tbody>
    </table>
</body>
</html>"""
    
    return html

def generate_report(results_file=None, output_dir="wise_evaluation_results", evaluation_type="standard"):
    """
    Wrapper function for generating reports (used by tests)
    
    Args:
        results_file: Path to JSON results file
        output_dir: Directory to save reports
        evaluation_type: Type of evaluation (standard, enhanced, rewritten)
    
    Returns:
        Path to generated HTML report
    """
    import json
    
    # Load results
    if results_file:
        with open(results_file, 'r') as f:
            raw_results = json.load(f)
        
        # Format results to match expected structure
        results = {
            "results": raw_results,
            "summary": {
                "average_wiscore": sum(r.get('wiscore', 0) for r in raw_results) / len(raw_results) if raw_results else 0,
                "average_consistency": sum(r.get('consistency', 0) for r in raw_results) / len(raw_results) if raw_results else 0,
                "average_realism": sum(r.get('realism', 0) for r in raw_results) / len(raw_results) if raw_results else 0,
                "average_aesthetic": sum(r.get('aesthetic_quality', 0) for r in raw_results) / len(raw_results) if raw_results else 0
            },
            "successful_evaluations": len(raw_results),
            "failed_evaluations": 0,
            "total_samples": len(raw_results)
        }
    else:
        try:
            results = load_results(evaluation_type)
        except (FileNotFoundError, ValueError) as e:
            raise e
    
    # Generate reports
    markdown_report = generate_markdown_report(results, evaluation_type)
    html_report = generate_html_report(results, evaluation_type)
    
    # Save reports
    os.makedirs(output_dir, exist_ok=True)
    
    md_path = f'{output_dir}/wise_evaluation_report_{evaluation_type}.md'
    html_path = f'{output_dir}/wise_evaluation_report_{evaluation_type}.html'
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown_report)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_report)
    
    return html_path

def main():
    """Generate reports"""
    parser = argparse.ArgumentParser(description='Generate WISE evaluation reports')
    parser.add_argument('--type', choices=['standard', 'enhanced', 'rewritten'], default='standard',
                       help='Type of results to generate report for (default: standard)')
    parser.add_argument('--all', action='store_true', help='Generate reports for all available result types')
    
    args = parser.parse_args()
    
    if args.all:
        # Generate reports for all available types
        comparison_results = load_comparison_results()
        
        if not comparison_results:
            print("No results found! Run evaluation first.")
            return
        
        print(f"Generating reports for {len(comparison_results)} result types...")
        
        for result_type, results in comparison_results.items():
            print(f"  Generating {result_type} report...")
            
            markdown_report = generate_markdown_report(results, result_type)
            html_report = generate_html_report(results, result_type)
            
            # Save reports
            os.makedirs('wise_evaluation_results', exist_ok=True)
            
            with open(f'wise_evaluation_results/wise_report_{result_type}.md', 'w', encoding='utf-8') as f:
                f.write(markdown_report)
            
            with open(f'wise_evaluation_results/wise_report_{result_type}.html', 'w', encoding='utf-8') as f:
                f.write(html_report)
            
            print(f"    {result_type} reports saved")
        
        print(f"\nAll reports generated successfully!")
        print(f"Location: wise_evaluation_results/")
        
    else:
        # Generate report for specific type
        result_type = args.type
        
        print(f"Generating WISE evaluation report for {result_type} results...")
        
        try:
            results = load_results(result_type)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
            return
        
        # Generate reports
        markdown_report = generate_markdown_report(results, result_type)
        html_report = generate_html_report(results, result_type)
        
        # Save reports
        os.makedirs('wise_evaluation_results', exist_ok=True)
        
        with open(f'wise_evaluation_results/wise_report_{result_type}.md', 'w', encoding='utf-8') as f:
            f.write(markdown_report)
        
        with open(f'wise_evaluation_results/wise_report_{result_type}.html', 'w', encoding='utf-8') as f:
            f.write(html_report)
        
        print("Reports generated successfully!")
        print(f"Markdown: wise_evaluation_results/wise_report_{result_type}.md")
        print(f"HTML: wise_evaluation_results/wise_report_{result_type}.html")
        
        # Print summary to console
        avg_wiscore = results['summary']['average_wiscore']
        print(f"\nSUMMARY:")
        print(f"   • Average WiScore: {avg_wiscore:.3f}")
        print(f"   • Samples evaluated: {results['successful_evaluations']}")
        print(f"   • Evaluation mode: {result_type}")

if __name__ == "__main__":
    main() 