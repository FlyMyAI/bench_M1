# WISE Bot Evaluation

This set of scripts allows you to evaluate the quality of your image generation bot using the WISE metric.

## Setup

1. Install required dependencies:
```bash
pip install openai requests python-dotenv matplotlib pandas
```
2. Create a `.env` file in the project root and add your OpenAI API and FlyMy API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
FLYMY_API_KEY=your_flymy_api_key_here
```

## Usage

### 1. Run Evaluation
```bash
python wise_bot_evaluation.py
```

This script will:
- Select random prompts from WISE datasets
- Generate images using your bot
- Evaluate them with GPT-4o using WISE criteria
- Calculate WiScore for each image
- Save results to `wise_evaluation_results/` folder

### 2. Analyze Results
```bash
python analyze_wise_results.py
```

This script creates:
- Detailed statistics by categories and subcategories
- Score distribution plots
- Correlation matrix of scores
- Detailed analysis in JSON format

## Results Structure

wise_evaluation_results/
├── images/ # Generated images
├── evaluation_results.json # Main evaluation results
├── detailed_analysis.json # Detailed statistical analysis
└── analysis_plots.png # Analysis charts

## WiScore Metric
WiScore is calculated using the formula:

```
WiScore = (0.7 × Consistency + 0.2 × Realism + 0.1 × Aesthetic Quality) / 2
```

Where each component is rated on a scale from 0 to 2:
- **Consistency**: How accurately the image reflects the prompt
- **Realism**: How realistic the image appears
- **Aesthetic Quality**: Overall artistic quality

## Configuration

In the `wise_bot_evaluation.py` file, you can modify:
- `NUM_SAMPLES`: number of samples for evaluation (default 10)
- Datasets for evaluation (cultural_common_sense, spatio-temporal_reasoning, natural_science)
- Image generation parameters

## Interpreting Results

- **WiScore > 0.5**: Excellent quality
- **WiScore 0.3-0.5**: Good quality  
- **WiScore 0.1-0.3**: Satisfactory quality
- **WiScore < 0.1**: Low quality

Compare your results with the WISE leaderboard to understand your bot's position relative to other models.

## Requirements

- Python 3.7+
- OpenAI API key (for evaluation using GPT-4o)
- Internet access for API calls
- WISE folder with datasets must be present in the project