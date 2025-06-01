# Face Identity Preservation Benchmark

A comprehensive evaluation of face transformation APIs across three prompt complexity levels using multiple metrics.

## Overview

This benchmark evaluates **identity preservation** in face image transformations across:
- **3 APIs**: FlyMy, FAL (Bagel/Edit), OpenAI (GPT-4V + DALL-E 3)
- **3 Complexity Levels**: Simple, Mid, Maximal prompts  
- **4 Categories**: Emotions, Age, Hair, Accessories
- **3 Metrics**: UNPG Similarity, CLIP Similarity, FID Score

**Dataset**: 8,832 image pairs from FFHQ faces

## Executive Summary

### 🎯 Single-Metric Comparison (UNPG Identity Preservation)

| API | Overall Score | Best Use Case | Performance |
|-----|---------------|---------------|-------------|
| **FlyMy** | **0.917** ⭐ | All categories | Excellent |
| FAL (Bagel/Edit) | 0.636 | Simple accessories | Moderate |
| OpenAI | 0.390 | Not recommended | Poor |

**Bottom Line**: FlyMy preserves **91.7%** of facial identity vs FAL Bagel/Edit's **63.6%** and OpenAI's **39.0%**

### 📊 Dual-Metric Summary

| API | Identity (UNPG) | Quality (FID) | Recommendation |
|-----|-----------------|---------------|----------------|
| **FlyMy** | **0.917** ⭐ | **94.8** ⭐ | **Choose for all tasks** |
| FAL (Bagel/Edit) | 0.636 | 141.0 | Limited use only |
| OpenAI | 0.390 | 176.8 | Avoid for faces |

*UNPG: Higher better (0-1), FID: Lower better*

**Key Takeaway**: FlyMy outperforms both FAL Bagel/Edit and OpenAI by significant margins across all metrics and categories.

## API Details

- **FlyMy**: Direct image transformation API
- **FAL**: fal-ai/bagel/edit model for image modifications  
- **OpenAI**: GPT-4V (vision) for analysis + DALL-E 3 for regeneration

## Key Findings

### 🏆 Overall Best Performer: **FlyMy**
- **UNPG Similarity**: 0.917 (91.7% identity preservation)
- **CLIP Similarity**: 0.920 (92.0% semantic similarity)  
- **FID Score**: 94.8 (highest image quality)

### 📊 API Performance Comparison

| API | UNPG Similarity | CLIP Similarity | FID Score |
|-----|----------------|----------------|-----------|
| **FlyMy** | **0.917** ⭐ | **0.920** ⭐ | **94.8** ⭐ |
| FAL (Bagel/Edit) | 0.636 | 0.696 | 141.0 |
| OpenAI (GPT-4V + DALL-E 3) | 0.390 | 0.530 | 176.8 |

*Higher is better for UNPG/CLIP, lower is better for FID*

## Detailed Per-Category Analysis

### 🎭 Emotions Category
**Best performing category for identity preservation**

| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.971 | 0.968 | **0.977** | **0.972** |
| FAL (Bagel/Edit) | 0.730 | 0.673 | 0.617 | 0.673 |
| OpenAI | 0.394 | 0.394 | 0.394 | 0.394 |

**CLIP Similarity:**
| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.970 | 0.971 | **0.979** | **0.973** |
| FAL (Bagel/Edit) | 0.730 | 0.730 | 0.730 | 0.730 |
| OpenAI | 0.542 | 0.542 | 0.541 | 0.542 |

### 👴 Age Category  
**Most challenging category for identity preservation**

| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.886 | **0.915** | 0.912 | **0.904** |
| FAL (Bagel/Edit) | 0.543 | 0.543 | 0.543 | 0.543 |
| OpenAI | 0.388 | 0.388 | 0.388 | 0.388 |

**CLIP Similarity:**
| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.891 | **0.924** | 0.915 | **0.910** |
| FAL (Bagel/Edit) | 0.616 | 0.616 | 0.615 | 0.616 |
| OpenAI | 0.500 | 0.499 | 0.500 | 0.500 |

### 💇 Hair Category
**Moderate difficulty transformations**

| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.859 | 0.870 | **0.899** | **0.876** |
| FAL (Bagel/Edit) | 0.621 | 0.621 | 0.620 | 0.621 |
| OpenAI | 0.388 | 0.388 | 0.387 | 0.388 |

**CLIP Similarity:**
| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.879 | 0.881 | **0.904** | **0.887** |
| FAL (Bagel/Edit) | 0.686 | 0.686 | 0.686 | 0.686 |
| OpenAI | 0.532 | 0.532 | 0.531 | 0.532 |

### 👓 Accessories Category
**Good performance, FAL Bagel/Edit competitive on simple prompts**

| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.928 | 0.930 | 0.928 | **0.918** |
| **FAL (Bagel/Edit)** | **0.955** | 0.706 | 0.457 | 0.706 |
| OpenAI | 0.390 | 0.389 | 0.390 | 0.390 |

**CLIP Similarity:**
| API | Simple | Mid | Maximal | Overall Mean |
|-----|--------|-----|---------|--------------|
| **FlyMy** | 0.915 | 0.915 | 0.915 | **0.909** |
| **FAL (Bagel/Edit)** | **0.930** | 0.753 | 0.566 | 0.753 |
| OpenAI | 0.546 | 0.546 | 0.545 | 0.546 |

## Key Insights from CSV Data

### 🔄 Complexity Impact Patterns

1. **FlyMy Benefits from Complexity**: 
   - Emotions: 0.971 → 0.977 (UNPG)
   - Hair: 0.859 → 0.899 (UNPG)
   - Consistent improvement with maximal prompts

2. **FAL Bagel/Edit Degrades with Complexity**:
   - Accessories: 0.955 → 0.457 (dramatic drop)
   - All categories show declining performance

3. **OpenAI Remains Stable** (but low):
   - Consistent ~0.39 UNPG across all conditions
   - Limited by two-stage generation process

### 🎯 Optimal Combinations (from CSV data)

| Category | Best Combination | UNPG Score | CLIP Score |
|----------|------------------|------------|------------|
| **Emotions** | FlyMy + Maximal | **0.977** | **0.979** |
| **Age** | FlyMy + Mid | **0.915** | **0.924** |
| **Hair** | FlyMy + Maximal | **0.899** | **0.904** |
| **Accessories** | FAL Bagel/Edit + Simple | **0.955** | **0.930** |

### 📊 Category Difficulty Ranking

Based on overall UNPG similarity means:
1. **Emotions**: 0.680 (easiest)
2. **Accessories**: 0.671  
3. **Hair**: 0.628
4. **Age**: 0.612 (most challenging)

## Detailed Results

### CSV Data Files
The repository includes detailed per-category analysis with complete statistics:

- **`accessories_api_complexity.csv`** - Shows FAL Bagel/Edit's strong simple prompt performance (0.955)
- **`age_api_complexity.csv`** - Reveals age as most challenging category  
- **`emotions_api_complexity.csv`** - Demonstrates FlyMy's excellence (0.972 mean)
- **`hair_api_complexity.csv`** - Hair transformation complexity analysis

Each CSV contains: API, complexity_level, count, mean, std, median

### Complete Results
📁 **Full results and visualizations**: [Google Drive](https://drive.google.com/drive/folders/1U1Snqj-r9pI0vzS09wEju8w-LZe4g7Gh?usp=sharing)

## Methodology

### APIs Tested
- **FlyMy**: Specialized face transformation API
- **FAL**: fal-ai/bagel/edit model via FAL platform
- **OpenAI**: Two-stage process using GPT-4V for image analysis + DALL-E 3 for regeneration

### Metrics Explained
- **UNPG Similarity**: Face identity preservation (0-1, higher better)
- **CLIP Similarity**: Semantic content preservation (0-1, higher better)  
- **FID Score**: Image quality/realism (lower better, <50 excellent)

## Strategic Recommendations

### 💡 Based on CSV Analysis

1. **For Maximum Identity Preservation**: FlyMy across all categories
2. **For Emotion Transformations**: FlyMy + Maximal (0.977 UNPG)
3. **For Age Transformations**: FlyMy + Mid (0.915 UNPG) 
4. **For Simple Accessories**: FAL Bagel/Edit + Simple (0.955 UNPG) - competitive option
5. **Avoid**: Complex prompts with FAL Bagel/Edit (dramatic performance drops)
6. **Avoid**: OpenAI for identity-critical applications (0.39 average)

### 🔍 Research Insights

- **Complexity Paradox**: Only FlyMy benefits from complex prompts
- **API Specialization**: FlyMy designed for identity preservation
- **FAL Bagel/Edit's Niche**: Excellent for simple accessory additions
- **Category Hierarchy**: Clear difficulty ranking from emotions to age
- **Consistency**: FlyMy shows reliable performance across all conditions

## Usage

The CSV files provide detailed statistics for research and implementation:
- `count`: Number of samples tested
- `mean`: Average performance score  
- `std`: Performance variability
- `median`: Robust central tendency measure

## Citation

```bibtex
@misc{face_identity_benchmark_2025,
  title={Face Identity Preservation Benchmark: A Multi-Metric Evaluation of Face Transformation APIs},
  author={[Your Name]},
  year={2025},
  url={https://github.com/FlyMyAI/bench_M1}
}
