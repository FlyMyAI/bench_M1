#!/usr/bin/env python3
"""
Configuration settings for WISE evaluation system.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
FLYMY_API_KEY = os.getenv('FLYMY_API_KEY') or os.getenv('API_KEY')  # Support both names

# API URLs
FLYMY_API_URL = "https://api.chat.flymy.ai/chat"

# WISE Evaluation Configuration
WISE_EVALUATION_CONFIG = {
    "model": "gpt-4o",
    "max_tokens": 500,
    "temperature": 0.1,
    "system_prompt": """You are an expert image evaluation system for the WISE benchmark. Evaluate the provided image against the given prompt using these criteria:

1. CONSISTENCY (0-2): How well does the image match the prompt description?
   - 0: Does not match the prompt at all
   - 1: Partially matches some elements of the prompt
   - 2: Accurately represents all key elements of the prompt

2. REALISM (0-2): How realistic and plausible does the image appear?
   - 0: Highly unrealistic, artificial, or distorted
   - 1: Somewhat realistic with minor issues
   - 2: Highly realistic and believable

3. AESTHETIC QUALITY (0-2): Overall visual appeal and composition
   - 0: Poor visual quality, composition, or appeal
   - 1: Average visual quality with room for improvement
   - 2: Excellent visual quality, composition, and appeal

Provide your evaluation in this exact format:
Consistency: [score]
Realism: [score]  
Aesthetic Quality: [score]

Then provide a brief explanation of your scoring."""
}


# Evaluation Settings
DEFAULT_SAMPLES_COUNT = 100
MAX_RETRIES = 3
TIMEOUT_SECONDS = 60

# Output Directories
RESULTS_DIR = "wise_evaluation_results"
IMAGES_DIR = "images"
REPORTS_DIR = "reports"

# File Paths
WISE_DATASET_FILES = [
    "WISE/data/cultural_common_sense.json",
    "WISE/data/spatio-temporal_reasoning.json", 
    "WISE/data/natural_science.json"
]

# FlyMy AI API settings
FLYMY_BASE_URL = "https://api.chat.flymy.ai"

# Test configuration
TEST_CONFIG = {
    "test_samples": 5,
    "comparison_enabled": True,
    "save_images": True,
    "detailed_logging": True
}

# Directories
TEST_IMAGES_DIR = f"{RESULTS_DIR}/test_images"

# Create directories
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(TEST_IMAGES_DIR, exist_ok=True) 