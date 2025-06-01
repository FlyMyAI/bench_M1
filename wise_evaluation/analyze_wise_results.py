import json
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

def analyze_wise_results(results_file="wise_evaluation_results/evaluation_results.json"):
    """Analyze and visualize WISE evaluation results"""
    
    if not Path(results_file).exists():
        print(f"Results file not found: {results_file}")
        return
    
    with open(results_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    summary = data['summary']
    results = data['individual_results']
    
    print("=== WISE Evaluation Analysis ===")
    print(f"Total samples: {data['total_samples']}")
    print(f"Successful evaluations: {data['successful_evaluations']}")
    print(f"Average WiScore: {summary['average_wiscore']:.3f}")
    print(f"Evaluation date: {data['evaluation_date']}")
    
    if not results:
        print("No results to analyze")
        return
    
    # Convert to DataFrame for easier analysis
    df = pd.DataFrame(results)
    
    # Extract individual scores
    df['consistency'] = df['scores'].apply(lambda x: x['consistency'])
    df['realism'] = df['scores'].apply(lambda x: x['realism'])
    df['aesthetic_quality'] = df['scores'].apply(lambda x: x['aesthetic_quality'])
    
    # Statistics by category
    print("\n=== Statistics by Category ===")
    if 'category' in df.columns and len(df['category'].unique()) > 1:
        category_stats = df.groupby('category').agg({
            'wiscore': ['mean', 'std', 'count'],
            'consistency': 'mean',
            'realism': 'mean',
            'aesthetic_quality': 'mean'
        }).round(3)
        print(category_stats)
    
    # Statistics by subcategory
    print("\n=== Statistics by Subcategory ===")
    if 'subcategory' in df.columns and len(df['subcategory'].unique()) > 1:
        subcategory_stats = df.groupby('subcategory').agg({
            'wiscore': ['mean', 'std', 'count'],
            'consistency': 'mean',
            'realism': 'mean',
            'aesthetic_quality': 'mean'
        }).round(3)
        print(subcategory_stats)
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # WiScore distribution
    axes[0, 0].hist(df['wiscore'], bins=10, alpha=0.7, color='blue')
    axes[0, 0].set_title('WiScore Distribution')
    axes[0, 0].set_xlabel('WiScore')
    axes[0, 0].set_ylabel('Frequency')
    
    # Individual scores comparison
    scores_data = [df['consistency'], df['realism'], df['aesthetic_quality']]
    axes[0, 1].boxplot(scores_data, tick_labels=['Consistency', 'Realism', 'Aesthetic'])
    axes[0, 1].set_title('Individual Scores Distribution')
    axes[0, 1].set_ylabel('Score')
    
    # WiScore by category
    if 'category' in df.columns and len(df['category'].unique()) > 1:
        category_means = df.groupby('category')['wiscore'].mean()
        axes[1, 0].bar(category_means.index, category_means.values)
        axes[1, 0].set_title('Average WiScore by Category')
        axes[1, 0].set_xlabel('Category')
        axes[1, 0].set_ylabel('Average WiScore')
        axes[1, 0].tick_params(axis='x', rotation=45)
    else:
        axes[1, 0].text(0.5, 0.5, 'Not enough categories\nfor comparison', 
                       ha='center', va='center', transform=axes[1, 0].transAxes)
        axes[1, 0].set_title('Average WiScore by Category')
    
    # Correlation matrix
    corr_data = df[['consistency', 'realism', 'aesthetic_quality', 'wiscore']].corr()
    im = axes[1, 1].imshow(corr_data, cmap='coolwarm', aspect='auto')
    axes[1, 1].set_xticks(range(len(corr_data.columns)))
    axes[1, 1].set_yticks(range(len(corr_data.columns)))
    axes[1, 1].set_xticklabels(corr_data.columns, rotation=45)
    axes[1, 1].set_yticklabels(corr_data.columns)
    axes[1, 1].set_title('Score Correlations')
    
    # Add correlation values to heatmap
    for i in range(len(corr_data.columns)):
        for j in range(len(corr_data.columns)):
            axes[1, 1].text(j, i, f'{corr_data.iloc[i, j]:.2f}', 
                           ha="center", va="center", color="black")
    
    plt.tight_layout()
    plt.savefig('wise_evaluation_results/analysis_plots.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Detailed results table
    print("\n=== Detailed Results ===")
    detailed_df = df[['sample_id', 'subcategory', 'wiscore', 'consistency', 'realism', 'aesthetic_quality']].round(3)
    print(detailed_df.to_string(index=False))
    
    # Save detailed analysis
    analysis_results = {
        'summary_statistics': {
            'mean_wiscore': float(df['wiscore'].mean()),
            'std_wiscore': float(df['wiscore'].std()),
            'min_wiscore': float(df['wiscore'].min()),
            'max_wiscore': float(df['wiscore'].max()),
            'mean_consistency': float(df['consistency'].mean()),
            'mean_realism': float(df['realism'].mean()),
            'mean_aesthetic': float(df['aesthetic_quality'].mean())
        }
    }
    
    if 'category' in df.columns and len(df['category'].unique()) > 1:
        category_stats = df.groupby('category').agg({
            'wiscore': ['mean', 'std', 'count'],
            'consistency': 'mean',
            'realism': 'mean',
            'aesthetic_quality': 'mean'
        }).round(3)
        # Convert to simple dict structure to avoid tuple keys
        analysis_results['category_breakdown'] = {
            str(category): {
                'wiscore_mean': float(stats['wiscore']['mean']),
                'wiscore_std': float(stats['wiscore']['std']) if not pd.isna(stats['wiscore']['std']) else 0.0,
                'count': int(stats['wiscore']['count']),
                'consistency_mean': float(stats['consistency']),
                'realism_mean': float(stats['realism']),
                'aesthetic_mean': float(stats['aesthetic_quality'])
            }
            for category, stats in category_stats.iterrows()
        }
    
    if 'subcategory' in df.columns and len(df['subcategory'].unique()) > 1:
        subcategory_stats = df.groupby('subcategory').agg({
            'wiscore': ['mean', 'std', 'count'],
            'consistency': 'mean',
            'realism': 'mean',
            'aesthetic_quality': 'mean'
        }).round(3)
        # Convert to simple dict structure to avoid tuple keys
        analysis_results['subcategory_breakdown'] = {
            str(subcategory): {
                'wiscore_mean': float(stats['wiscore']['mean']),
                'wiscore_std': float(stats['wiscore']['std']) if not pd.isna(stats['wiscore']['std']) else 0.0,
                'count': int(stats['wiscore']['count']),
                'consistency_mean': float(stats['consistency']),
                'realism_mean': float(stats['realism']),
                'aesthetic_mean': float(stats['aesthetic_quality'])
            }
            for subcategory, stats in subcategory_stats.iterrows()
        }
    
    with open('wise_evaluation_results/detailed_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, ensure_ascii=False, indent=2)
    
    print("\nAnalysis complete! Check 'wise_evaluation_results/' for detailed outputs.")

if __name__ == "__main__":
    analyze_wise_results() 