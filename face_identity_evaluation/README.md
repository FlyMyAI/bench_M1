# Face Identity Preservation Benchmark

A comprehensive evaluation of face transformation APIs across three prompt complexity levels using multiple metrics.

## Overview

This benchmark evaluates **identity preservation** in face image transformations across:
- **3 APIs**: FlyMy, Bagel/Edit, OpenAI (GPT-4V + DALL-E 3)
- **3 Complexity Levels**: Simple, Mid, Maximal prompts  
- **4 Categories**: Emotions, Age, Hair, Accessories
- **3 Metrics**: UNPG Similarity, CLIP Similarity, FID Score

**Dataset**: First 50 images from FFHQ dataset. For each API, we generated approximately **1,000 transformed images** (50 base images × 20 prompts), totaling **8,832 transformation pairs** across all APIs and complexity levels.

## Executive Summary

### 🎯 Single Number Comparison (Identity Preservation)

| API | Overall Score | Advantage |
|-----|---------------|-----------|
| **FlyMy** | **0.917** ⭐ | **+44% vs FAL, +135% vs OpenAI** |
| Bagel/Edit | 0.636 | +63% vs OpenAI |
| OpenAI | 0.390 | Baseline |

### 📊 Quick Comparison

| Metric | FlyMy | FAL (Bagel/Edit) | OpenAI | Winner |
|--------|-------|------------------|--------|---------|
| **Identity** | 0.917 | 0.636 | 0.390 | FlyMy |
| **Quality** | 94.8 | 141.0 | 176.8 | FlyMy |
| **Semantics** | 0.920 | 0.696 | 0.530 | FlyMy |

**Bottom Line**: FlyMy dominates all metrics. Use FlyMy for face transformations.

## Detailed Results by Category

### Performance Summary

| Category | FlyMy | FAL | OpenAI | Best API |
|----------|-------|-----|--------|----------|
| **Emotions** | 0.972 | 0.673 | 0.394 | FlyMy (+45%) |
| **Accessories** | 0.918 | 0.706 | 0.390 | FlyMy (+30%) |
| **Hair** | 0.876 | 0.621 | 0.388 | FlyMy (+41%) |
| **Age** | 0.904 | 0.543 | 0.388 | FlyMy (+66%) |

### Complexity Impact

| API | Simple → Maximal | Trend |
|-----|------------------|--------|
| **FlyMy** | 0.903 → 0.929 | **Improves +3%** ⬆️ |
| Bagel/Edit | 0.857 → 0.457 | Degrades -47% ⬇️ |
| OpenAI | 0.385 → 0.383 | Stable (poor) → |

### Best Use Cases

| Use Case | Optimal Choice | Score |
|----------|----------------|--------|
| **Emotion changes** | FlyMy + Maximal | 0.977 |
| **Age transformations** | FlyMy + Mid | 0.915 |
| **Hair styling** | FlyMy + Maximal | 0.899 |
| **Simple accessories** | Bagel/Edit + Simple | 0.955 |

## Key Insights

### 💡 Strategic Recommendations

1. **Default choice**: FlyMy for all face transformations
2. **Complex prompts**: Only beneficial with FlyMy
3. **Simple accessories**: Bagel/Edit competitive (0.955 vs 0.928)
4. **Avoid**: OpenAI for identity-critical applications
5. **Category difficulty**: Age > Hair > Accessories > Emotions

### 🔍 Technical Findings

- **FlyMy**: Specialized for identity preservation, benefits from complexity
- **Bagel/Edit**: Good for simple edits, degrades with complex prompts  
- **OpenAI**: Two-stage process limits identity preservation
- **Emotions**: Easiest category (0.680 avg)
- **Age**: Most challenging category (0.612 avg)

## Data & Methodology

### Dataset
- **Source**: First 50 images from FFHQ dataset
- **Per API**: ~1,000 generated images (50 base × 20 prompts)
- **Total pairs**: 8,832 image comparisons across all APIs
- **Transformations**: 20 prompts × 3 complexity levels × 3 APIs

### APIs Tested
- **FlyMy**: Chat agent with SOTA face editing models
- **FAL**: fal-ai/bagel/edit model
- **OpenAI**: GPT-4V analysis + DALL-E 3 generation

### Metrics
- **UNPG**: Identity preservation (0-1, higher better)
- **CLIP**: Semantic similarity (0-1, higher better)  
- **FID**: Image quality (lower better)

## Complete Results & Data

📁 **Full benchmark data available on Google Drive**: [Benchmark Results](https://drive.google.com/drive/folders/1U1Snqj-r9pI0vzS09wEju8w-LZe4g7Gh?usp=sharing)

**Includes:**
- Detailed CSV files with per-image statistics
- Generated images for all 8,832 transformation pairs
- Comparison tables and analysis breakdowns
- Raw metric calculations for reproducibility

## Citation

```bibtex
@misc{face_identity_benchmark_2025,
 title={Face Identity Preservation Benchmark: A Multi-Metric Evaluation of Face Transformation APIs},
 year={2025},
 url={https://github.com/FlyMyAI/bench_M1}
}
