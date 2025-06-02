# GenEval Image Generation Evaluation

This directory contains the complete GenEval benchmark evaluation for **Flymy AI** image generation model.

## Results Summary

| Metric | Value |
|--------|--------|
| **Overall Image Accuracy** | **76.16%** (1680/2206) |
| **Prompt Accuracy** | **60.69%** (335/552) |
| **Overall Score** | **0.7690** |

## GenEval Benchmark Results Comparison

| Type | Model | Single Obj. | Two Obj. | Counting | Colors | Position | Color Attr. | Overall |
|------|-------|-------------|----------|----------|---------|----------|-------------|---------|
| **Gen. Only** | PixArt-α [9] | 0.98 | 0.50 | 0.44 | 0.80 | 0.08 | 0.07 | 0.48 |
| | SDv2.1 [61] | 0.98 | 0.51 | 0.44 | 0.85 | 0.07 | 0.17 | 0.50 |
| | DALL-E 2 [60] | 0.94 | 0.66 | 0.49 | 0.77 | 0.10 | 0.19 | 0.52 |
| | Emu3-Gen [79] | 0.98 | 0.71 | 0.34 | 0.81 | 0.17 | 0.21 | 0.54 |
| | SDXL [58] | 0.98 | 0.74 | 0.39 | 0.85 | 0.15 | 0.23 | 0.55 |
| | DALL-E 3 [5] | 0.96 | 0.87 | 0.47 | 0.83 | 0.43 | 0.45 | 0.67 |
| | SD3-Medium [19] | 0.99 | 0.94 | 0.72 | 0.89 | 0.33 | 0.60 | 0.74 |
| | FLUX.1-dev† [35] | 0.98 | 0.93 | 0.75 | **0.93** | 0.68 | 0.65 | 0.82 |
| **Unified** | Chameleon [70] | - | - | - | - | - | - | 0.39 |
| | LWM [42] | 0.93 | 0.41 | 0.46 | 0.79 | 0.09 | 0.15 | 0.47 |
| | SEED-X [23] | 0.97 | 0.58 | 0.26 | 0.80 | 0.19 | 0.14 | 0.49 |
| | TokenFlow-XL [59] | 0.95 | 0.60 | 0.41 | 0.81 | 0.16 | 0.24 | 0.55 |
| | ILLUME [76] | 0.99 | 0.86 | 0.45 | 0.71 | 0.39 | 0.28 | 0.61 |
| | Janus [83] | 0.97 | 0.68 | 0.30 | 0.84 | 0.46 | 0.42 | 0.61 |
| | Transfusion [102] | - | - | - | - | - | - | 0.63 |
| | Emu3-Gen [79] | 0.99 | 0.81 | 0.42 | 0.80 | 0.49 | 0.45 | 0.66 |
| | Show-o [88] | 0.98 | 0.80 | 0.66 | 0.84 | 0.31 | 0.50 | 0.68 |
| | Janus-Pro-7B [1] | 0.99 | 0.89 | 0.59 | 0.90 | **0.79** | 0.66 | 0.80 |
| | MetaQuery-XL† [57] | - | - | - | - | - | - | 0.80 |
| | BAGEL | 0.99 | 0.94 | **0.81** | 0.88 | **0.64** | 0.63 | **0.82** |
| | **Flymy AI M1** | **1.00** | **0.98** | 0.79 | 0.91 | 0.60 | **0.72** | **0.83** |

## Usage

### Generate Images
```bash
python gen_images_flymy.py \
    --output_dir output/images \
    --metadata_file evaluation_metadata.jsonl \
    --num_images 4 \
    --num_workers 1
```

### Run Evaluation
```bash
python evaluate_images_single.py \
    output/images \
    --outfile results.jsonl
```

### Generate Reports
```bash
python generate_report.py \
    results.jsonl \
    --output report.md \
    --model-name "Flymy AI" \
    --csv
```

## 📁 Directory Structure

```
gen_evaluation/
├── README.md                          # This file
├── gen_images_flymy.py                # Image generation script
├── evaluate_images_single.py          # Evaluation script
├── generate_report.py                 # Report generation
├── evaluation_metadata.jsonl          # Evaluation prompts
├── object_names.txt                   # Object class names
├── mask2former_swin-s-p4-w7-224...pth # Object detection model (symlink)
├── geneval_comparison_table.md        # Benchmark comparison
├── full_evaluation_report.md          # Detailed report
├── geneval_summary.csv                # Summary metrics
├── geneval_categories.csv             # Category breakdown
├── geneval_prompts.csv                # Per-prompt results
└── geneval_errors.csv                 # Error analysis
```
