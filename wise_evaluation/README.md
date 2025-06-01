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

Each metric is scored on a 0-2 scale:
- **Consistency**: Alignment between prompt and generated image
- **Realism**: Visual quality and believability
- **Aesthetic Quality**: Artistic appeal and composition

## Benchmark Comparison

The system automatically compares your model against 18 state-of-the-art models from the WISE paper, including:

### Top Performers
- **FLUX.1-dev**: 0.500 WiScore
- **playground-v2.5**: 0.490 WiScore  
- **FLUX.1-schnell**: 0.480 WiScore

### Popular Models
- **DALL-E 3**: 0.430 WiScore
- **Midjourney-v6**: 0.440 WiScore
- **Stable Diffusion XL**: 0.450 WiScore

## Output Files

### Results
- `wise_evaluation_results/evaluation_results.json` - Complete evaluation data
- Progress is saved after each sample evaluation

### Reports  
- `wise_evaluation_results/wise_report.md` - Markdown analysis report
- `wise_evaluation_results/wise_report.html` - Interactive HTML report

### Images
- `wise_evaluation_results/images/` - Generated images with sample IDs

## Advanced Usage

### Generate Analysis Reports
```bash
python analyze_wise_results.py
```

### Create Detailed Report
```bash
python generate_wise_report.py
```

### Monitor Real-time Progress
```bash
python check_progress.py
```

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
- Internet connection for API calls

## Contributing

This evaluation system is designed to be model-agnostic. To integrate with other text-to-image APIs, modify the `bot_api.py` interface while maintaining the same return format.

## License

Part of the bench_M1 benchmark collection for evaluating AI image generation models. 