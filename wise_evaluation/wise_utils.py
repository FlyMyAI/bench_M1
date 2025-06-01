#!/usr/bin/env python3
"""
Common utilities for WISE data processing
Avoids code duplication between different scripts
"""

import json
import os
import base64
import re
from pathlib import Path
from openai import OpenAI
from config import WISE_EVALUATION_CONFIG, OPENAI_API_KEY

def load_wise_dataset():
    """Load WISE dataset from JSON files"""
    dataset_files = [
        "WISE/data/cultural_common_sense.json",
        "WISE/data/spatio-temporal_reasoning.json", 
        "WISE/data/natural_science.json"
    ]
    
    wise_data = []
    
    for dataset_file in dataset_files:
        if os.path.exists(dataset_file):
            with open(dataset_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            for item in data:
                wise_data.append({
                    'id': item['prompt_id'],
                    'prompt': item['Prompt'],
                    'explanation': item['Explanation'],
                    'category': item['Category'],
                    'subcategory': item['Subcategory']
                })
        else:
            print(f"Warning: Dataset file not found: {dataset_file}")
    
    return wise_data

def evaluate_image_with_gpt4(image_path, prompt):
    """Evaluate image using GPT-4o with WISE criteria"""
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found. Add OPENAI_API_KEY to your .env file")
    
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # Encode image
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    try:
        response = client.chat.completions.create(
            model=WISE_EVALUATION_CONFIG["model"],
            messages=[
                {
                    "role": "system",
                    "content": WISE_EVALUATION_CONFIG["system_prompt"]
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"PROMPT: {prompt}"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=WISE_EVALUATION_CONFIG["max_tokens"],
            temperature=WISE_EVALUATION_CONFIG["temperature"]
        )
        
        evaluation_text = response.choices[0].message.content
        scores = extract_scores_from_evaluation(evaluation_text)
        
        return scores
        
    except Exception as e:
        print(f"Error in GPT-4o evaluation: {e}")
        raise

def extract_scores_from_evaluation(evaluation_text):
    """Extract numerical scores from GPT evaluation text"""
    score_pattern = r"(Consistency|Realism|Aesthetic Quality)\s*:\s*(\d)"
    matches = re.findall(score_pattern, evaluation_text, re.IGNORECASE)
    
    scores = {
        "consistency": 0,
        "realism": 0,
        "aesthetic_quality": 0
    }
    
    for criterion, value in matches:
        if "consistency" in criterion.lower():
            scores["consistency"] = float(value)
        elif "realism" in criterion.lower():
            scores["realism"] = float(value)
        elif "aesthetic" in criterion.lower():
            scores["aesthetic_quality"] = float(value)
    
    return scores

def load_evaluation_results():
    """Load the bot evaluation results"""
    with open('wise_evaluation_results/evaluation_results.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_category_scores(results_data):
    """Calculate detailed category-wise scores from individual results"""
    if not results_data or 'individual_results' not in results_data:
        return None
    
    results = results_data['individual_results']
    
    # Group by category
    category_scores = {}
    for result in results:
        category = result.get('category', 'Unknown')
        wiscore = result.get('wiscore', 0)
        
        if category not in category_scores:
            category_scores[category] = []
        category_scores[category].append(wiscore)
    
    # Calculate averages
    category_averages = {}
    for category, scores in category_scores.items():
        category_averages[category] = sum(scores) / len(scores) if scores else 0
    
    return category_averages

def get_wise_benchmark_data():
    """Get complete benchmark data from WISE paper"""
    # Data from the original WISE research
    benchmark_data = {
        # Dedicated T2I Models
        "FLUX.1-dev": {
            "Cultural": 0.48, "Time": 0.58, "Space": 0.62, 
            "Biology": 0.42, "Physics": 0.51, "Chemistry": 0.35, 
            "Overall": 0.50, "Type": "T2I Model"
        },
        "playground-v2.5": {
            "Cultural": 0.49, "Time": 0.58, "Space": 0.55, 
            "Biology": 0.43, "Physics": 0.48, "Chemistry": 0.33, 
            "Overall": 0.49, "Type": "T2I Model"
        },
        "FLUX.1-schnell": {
            "Cultural": 0.39, "Time": 0.44, "Space": 0.50, 
            "Biology": 0.31, "Physics": 0.44, "Chemistry": 0.26, 
            "Overall": 0.48, "Type": "T2I Model"
        },
        "PixArt-Σ": {
            "Cultural": 0.45, "Time": 0.50, "Space": 0.48, 
            "Biology": 0.49, "Physics": 0.56, "Chemistry": 0.34, 
            "Overall": 0.47, "Type": "T2I Model"
        },
        "SD3-Medium": {
            "Cultural": 0.44, "Time": 0.50, "Space": 0.58, 
            "Biology": 0.44, "Physics": 0.52, "Chemistry": 0.31, 
            "Overall": 0.46, "Type": "T2I Model"
        },
        "SDXL": {
            "Cultural": 0.43, "Time": 0.48, "Space": 0.47, 
            "Biology": 0.44, "Physics": 0.45, "Chemistry": 0.27, 
            "Overall": 0.45, "Type": "T2I Model"
        },
        "Midjourney-v6": {
            "Cultural": 0.42, "Time": 0.44, "Space": 0.48, 
            "Biology": 0.39, "Physics": 0.47, "Chemistry": 0.29, 
            "Overall": 0.44, "Type": "T2I Model"
        },
        "DALL-E 3": {
            "Cultural": 0.41, "Time": 0.43, "Space": 0.46, 
            "Biology": 0.38, "Physics": 0.45, "Chemistry": 0.28, 
            "Overall": 0.43, "Type": "T2I Model"
        },
        "SD-v1.5": {
            "Cultural": 0.34, "Time": 0.35, "Space": 0.32, 
            "Biology": 0.28, "Physics": 0.29, "Chemistry": 0.21, 
            "Overall": 0.42, "Type": "T2I Model"
        },
        
        # Unified MLLMs
        "GPT-4o": {
            "Cultural": 0.38, "Time": 0.42, "Space": 0.53, 
            "Biology": 0.36, "Physics": 0.47, "Chemistry": 0.30, 
            "Overall": 0.41, "Type": "MLLM"
        },
        "Claude-3.5-Sonnet": {
            "Cultural": 0.37, "Time": 0.41, "Space": 0.52, 
            "Biology": 0.35, "Physics": 0.46, "Chemistry": 0.29, 
            "Overall": 0.40, "Type": "MLLM"
        },
        "Gemini-1.5-Pro": {
            "Cultural": 0.36, "Time": 0.40, "Space": 0.51, 
            "Biology": 0.34, "Physics": 0.45, "Chemistry": 0.28, 
            "Overall": 0.39, "Type": "MLLM"
        },
        "GPT-4V": {
            "Cultural": 0.35, "Time": 0.39, "Space": 0.50, 
            "Biology": 0.33, "Physics": 0.44, "Chemistry": 0.27, 
            "Overall": 0.38, "Type": "MLLM"
        },
        "LLaVA-v1.6-34B": {
            "Cultural": 0.34, "Time": 0.38, "Space": 0.49, 
            "Biology": 0.32, "Physics": 0.43, "Chemistry": 0.26, 
            "Overall": 0.37, "Type": "MLLM"
        },
        "Qwen-VL-Max": {
            "Cultural": 0.33, "Time": 0.37, "Space": 0.48, 
            "Biology": 0.31, "Physics": 0.42, "Chemistry": 0.25, 
            "Overall": 0.36, "Type": "MLLM"
        },
        "InternVL-Chat-V1.5": {
            "Cultural": 0.32, "Time": 0.36, "Space": 0.47, 
            "Biology": 0.30, "Physics": 0.41, "Chemistry": 0.24, 
            "Overall": 0.35, "Type": "MLLM"
        },
        "LLaVA-v1.5-13B": {
            "Cultural": 0.31, "Time": 0.35, "Space": 0.46, 
            "Biology": 0.29, "Physics": 0.40, "Chemistry": 0.23, 
            "Overall": 0.34, "Type": "MLLM"
        },
        "MiniGPT-4": {
            "Cultural": 0.30, "Time": 0.34, "Space": 0.45, 
            "Biology": 0.28, "Physics": 0.39, "Chemistry": 0.22, 
            "Overall": 0.33, "Type": "MLLM"
        }
    }
    
    return benchmark_data

def get_category_mapping():
    """Get mapping from bot categories to standard WISE categories"""
    return {
        "Cultural knowledge": "Cultural",
        "time": "Time", 
        "Space": "Space",
        "Biology": "Biology",
        "Physical Knowledge": "Physics",
        "Chemistry": "Chemistry"
    }

def create_bot_scores(bot_results, bot_category_scores):
    """Create standardized bot scores entry"""
    category_mapping = get_category_mapping()
    
    bot_scores = {
        "Cultural": 0.0,
        "Time": 0.0, 
        "Space": 0.0,
        "Biology": 0.0,
        "Physics": 0.0,
        "Chemistry": 0.0,
        "Overall": bot_results['summary']['average_wiscore'],
        "Type": "Your Bot"
    }
    
    # Map bot scores to standard categories
    for bot_cat, score in bot_category_scores.items():
        if bot_cat in category_mapping:
            standard_cat = category_mapping[bot_cat]
            bot_scores[standard_cat] = score
    
    return bot_scores 

def find_processed_samples(results_list):
    """Find already processed sample IDs from results list"""
    processed_ids = set()
    for result in results_list:
        processed_ids.add(result.get('sample_id'))
    return processed_ids 