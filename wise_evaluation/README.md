# WISE Evaluation System for Text-to-Image Models

A comprehensive evaluation system for text-to-image models using the WISE (World knowledge-based Image generation and editing benchmarK) benchmark. This system evaluates image generation quality across multiple categories including cultural knowledge, temporal reasoning, spatial understanding, and scientific accuracy.

## Features

- **WISE Benchmark Integration**: Complete integration with WISE dataset covering 6 knowledge domains
- **GPT-4o Evaluation**: Automated scoring using GPT-4o for consistency, realism, and aesthetic quality
- **Real-time Progress Saving**: Results are saved after each evaluation to prevent data loss
- **Comprehensive Reporting**: Detailed analysis with category breakdowns and benchmark comparisons
- **Model Information Tracking**: Records which model was used for each evaluation

## Installation

1. Navigate to the wise_evaluation directory:
```bash
cd wise_evaluation
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp env_example.txt .env
```

Edit `.env` file with your API keys:
```
FLYMY_API_KEY=your_flymy_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

4. Initialize WISE dataset (if using git submodules):
```bash
git submodule update --init --recursive
```

## Quick Start

### Basic Evaluation (5 samples)
```bash
python wise_bot_evaluation.py --samples 5
```

### Diverse Sampling (100 samples from all categories)
```bash
python wise_bot_evaluation.py --samples 100
```

### Continue Interrupted Evaluation
```bash
python wise_bot_evaluation.py --continue --samples 100
```

### Check Progress During Evaluation
```bash
python check_progress.py
```

## WISE Dataset Structure

The evaluation covers **1000 prompts** across **6 major categories**:

- **Cultural Knowledge** (400 samples): Festivals, traditions, art, customs
- **Temporal Reasoning** (167 samples): Seasonal changes, time relationships
- **Spatial Understanding** (133 samples): Perspective, occlusion, positioning  
- **Biology** (100 samples): Life processes, anatomy, ecosystems
- **Physical Knowledge** (100 samples): Physics, mechanics, thermodynamics
- **Chemistry** (100 samples): Chemical processes, reactions, materials

## Evaluation Metrics

### WiScore Calculation
WiScore = (0.7 × Consistency + 0.2 × Realism + 0.1 × Aesthetic Quality) / 2

## Key Features

✅ **Fault Tolerance**: Results saved after each evaluation  
✅ **Resume Capability**: Continue from any interruption point  
✅ **Model Tracking**: Records API and model information  
✅ **Category Analysis**: Detailed breakdown by knowledge domain  
✅ **Benchmark Integration**: Compare against 18 SOTA models  
✅ **Real-time Monitoring**: Track progress without interrupting evaluation

## File Structure

```
wise_evaluation/
├── wise_bot_evaluation.py     # Main evaluation script
├── wise_utils.py             # Utility functions
├── bot_api.py               # FlyMy AI API interface
├── config.py                # Configuration settings
├── analyze_wise_results.py  # Results analysis
├── generate_wise_report.py  # Report generation
├── check_progress.py        # Progress monitoring
├── WISE/                    # WISE dataset (submodule)
├── wise_evaluation_results/ # Output directory
└── requirements.txt         # Dependencies
```

## Requirements

- Python 3.8+
- OpenAI API key (for GPT-4o evaluation)
- FlyMy AI API key (for image generation)

## WISE Benchmark Results

| Type | Model | Cultural | Time | Space | Biology | Physics | Chemistry | Overall |
|------|-------|----------|------|-------|---------|---------|-----------|---------|
| **Gen-Only** | SDv1.5 | 0.34 | 0.35 | 0.32 | 0.28 | 0.29 | 0.21 | **0.32** |
| | SDXL | 0.43 | 0.48 | 0.47 | 0.44 | 0.45 | 0.27 | **0.43** |
| | SD3.5-large | 0.44 | 0.50 | 0.58 | 0.44 | 0.52 | 0.31 | **0.46** |
| | PixArt-Alpha | 0.45 | 0.50 | 0.48 | 0.49 | 0.56 | 0.34 | **0.47** |
| | playground-v2.5 | 0.49 | 0.58 | 0.55 | 0.43 | 0.48 | 0.33 | **0.49** |
| | FLUX.1-dev | 0.48 | 0.58 | 0.62 | 0.42 | 0.51 | 0.35 | **0.50** |
| **Unified** | Janus | 0.16 | 0.26 | 0.35 | 0.28 | 0.30 | 0.14 | **0.23** |
| | VILA-U | 0.26 | 0.33 | 0.37 | 0.35 | 0.39 | 0.23 | **0.31** |
| | Show-o-512 | 0.28 | 0.40 | 0.48 | 0.30 | 0.46 | 0.30 | **0.35** |
| | Janus-Pro-7B | 0.30 | 0.37 | 0.49 | 0.36 | 0.42 | 0.26 | **0.35** |
| | Emu3 | 0.34 | 0.45 | 0.48 | 0.41 | 0.45 | 0.27 | **0.39** |
| | MetaQuery-XL | 0.56 | 0.55 | 0.62 | 0.49 | 0.63 | 0.41 | **0.55** |
| | GPT-4o** | 0.81 | 0.71 | 0.89 | 0.83 | 0.79 | 0.74 | **0.80** |
| | BAGEL | 0.44 | 0.55 | 0.68 | 0.44 | 0.60 | 0.39 | **0.52** |
| | BAGEL w/ Self-CoT | 0.76 | 0.69 | 0.75 | 0.65 | 0.75 | 0.58 | **0.70** |
| | **FlyMy AI Bot** | **0.791** | **0.926** | **0.876** | **0.838** | **0.910** | **0.841** | **0.864** | 


## License

Part of the bench_M1 benchmark collection for evaluating AI image generation models. 