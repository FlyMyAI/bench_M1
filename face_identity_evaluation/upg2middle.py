import json
import os
from copy import deepcopy

def enhance_prompts_for_apis(simple_prompts_file, output_dir="enhanced_prompts"):
    """
    Enhance simple prompts to mid-level complexity for different APIs
    
    Args:
        simple_prompts_file: Path to the simple prompts JSON file
        output_dir: Directory to save enhanced prompt files
    """
    
    # Load simple prompts
    with open(simple_prompts_file, 'r') as f:
        base_config = json.load(f)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Enhancement strategies for each API
    api_enhancements = {
        "flymy": {
            "prefix": "preserve facial features and identity, ",
            "suffix": ", maintain natural skin texture and facial bone structure, realistic lighting",
            "style": "detailed_descriptive"
        },
        "fal": {
            "prefix": "high quality portrait, ",
            "suffix": ", photorealistic, professional photography, maintain person's unique features",
            "style": "technical_precise"
        },
        "openai": {
            "prefix": "portrait photograph, ",
            "suffix": ", natural expression, preserve distinctive facial characteristics, studio lighting",
            "style": "photographic_natural"
        }
    }
    
    # Category-specific enhancements
    category_enhancements = {
        "emotions": {
            "flymy": {
                "descriptors": ["with authentic micro-expressions", "showing genuine emotion", "natural facial muscle movement", 
                             "expressive eyes and mouth", "subtle emotional nuances"],
                "contexts": ["in natural lighting", "with soft shadows", "professional portrait style"]
            },
            "fal": {
                "descriptors": ["detailed facial expression", "realistic emotion rendering", "precise muscle tension", 
                             "accurate eye movement", "natural lip positioning"],
                "contexts": ["high resolution", "sharp focus", "professional quality"]
            },
            "openai": {
                "descriptors": ["natural emotional expression", "genuine feeling", "realistic facial movement", 
                             "authentic human emotion", "lifelike expression"],
                "contexts": ["portrait photography style", "natural lighting", "professional composition"]
            }
        },
        "age": {
            "flymy": {
                "descriptors": ["with appropriate skin texture for age", "realistic aging process", "natural wrinkle patterns", 
                             "age-appropriate features", "convincing age transformation"],
                "contexts": ["maintaining facial structure", "preserving unique characteristics", "natural aging"]
            },
            "fal": {
                "descriptors": ["accurate age progression", "realistic skin aging", "proper facial maturation", 
                             "age-consistent features", "natural aging effects"],
                "contexts": ["high detail", "realistic rendering", "precise age mapping"]
            },
            "openai": {
                "descriptors": ["natural age appearance", "realistic aging", "authentic age features", 
                             "believable age transformation", "natural maturation"],
                "contexts": ["portrait style", "natural appearance", "realistic aging process"]
            }
        },
        "hair": {
            "flymy": {
                "descriptors": ["with natural hair texture", "realistic hair styling", "proper hair volume and flow", 
                             "convincing hair transformation", "natural hair appearance"],
                "contexts": ["maintaining face shape harmony", "professional styling", "realistic hair physics"]
            },
            "fal": {
                "descriptors": ["detailed hair rendering", "accurate hair structure", "realistic hair properties", 
                             "precise hair modeling", "natural hair dynamics"],
                "contexts": ["high resolution hair", "detailed strands", "realistic hair lighting"]
            },
            "openai": {
                "descriptors": ["natural hair styling", "realistic hair texture", "authentic hair appearance", 
                             "believable hair change", "natural hair flow"],
                "contexts": ["professional hair styling", "natural hair movement", "realistic hair lighting"]
            }
        },
        "accessories": {
            "flymy": {
                "descriptors": ["with properly fitted accessories", "realistic accessory placement", "natural interaction with face", 
                             "convincing accessory integration", "seamless accessory addition"],
                "contexts": ["maintaining facial proportions", "realistic shadows and reflections", "natural accessory physics"]
            },
            "fal": {
                "descriptors": ["precisely positioned accessories", "accurate accessory rendering", "realistic material properties", 
                             "detailed accessory modeling", "proper accessory integration"],
                "contexts": ["high detail accessories", "realistic materials", "accurate placement"]
            },
            "openai": {
                "descriptors": ["naturally worn accessories", "realistic accessory fit", "authentic accessory style", 
                             "believable accessory addition", "natural accessory integration"],
                "contexts": ["portrait photography with accessories", "natural accessory lighting", "realistic accessory appearance"]
            }
        }
    }
    
    # Generate enhanced prompts for each API
    for api_name, api_config in api_enhancements.items():
        enhanced_config = deepcopy(base_config)
        enhanced_config["benchmark_info"]["name"] = f"Face Identity Preservation Benchmark - Mid Level ({api_name.upper()})"
        enhanced_config["benchmark_info"]["version"] = f"1.0-mid-{api_name}"
        
        # Enhance each category
        for category_name, category_data in enhanced_config["categories"].items():
            category_enhancement = category_enhancements[category_name][api_name]
            
            # Enhance prompts in each intensity level
            for intensity_level in ["intensity_1_subtle", "intensity_2_moderate", "intensity_3_intense"]:
                if intensity_level in category_data and category_data[intensity_level]:
                    for prompt_data in category_data[intensity_level]:
                        original_prompt = prompt_data["prompt"]
                        
                        # Build enhanced prompt
                        enhanced_prompt = enhance_single_prompt(
                            original_prompt,
                            api_config,
                            category_enhancement,
                            prompt_data["expected_difficulty"]
                        )
                        
                        prompt_data["prompt"] = enhanced_prompt
                        prompt_data["enhancement_level"] = "mid"
                        prompt_data["api_optimized"] = api_name
        
        # Save enhanced prompts for this API
        output_file = os.path.join(output_dir, f"prompts_mid_{api_name}.json")
        with open(output_file, 'w') as f:
            json.dump(enhanced_config, f, indent=2)
        
        print(f"Enhanced prompts for {api_name.upper()} saved to: {output_file}")

def enhance_single_prompt(original_prompt, api_config, category_enhancement, difficulty):
    """
    Enhance a single prompt based on API and category specifications
    """
    import random
    
    # Select enhancement elements based on difficulty
    if difficulty == "easy":
        num_descriptors = 1
        num_contexts = 1
    elif difficulty == "medium":
        num_descriptors = 2
        num_contexts = 1
    elif difficulty == "hard":
        num_descriptors = 2
        num_contexts = 2
    else:  # very_hard
        num_descriptors = 3
        num_contexts = 2
    
    # Randomly select descriptors and contexts
    selected_descriptors = random.sample(
        category_enhancement["descriptors"], 
        min(num_descriptors, len(category_enhancement["descriptors"]))
    )
    selected_contexts = random.sample(
        category_enhancement["contexts"], 
        min(num_contexts, len(category_enhancement["contexts"]))
    )
    
    # Build enhanced prompt
    enhanced_parts = [api_config["prefix"]]
    enhanced_parts.append(original_prompt.lower())
    enhanced_parts.extend(selected_descriptors)
    enhanced_parts.extend(selected_contexts)
    enhanced_parts.append(api_config["suffix"])
    
    # Join and clean up
    enhanced_prompt = ", ".join(part.strip() for part in enhanced_parts if part.strip())
    
    # Clean up duplicate commas and spaces
    enhanced_prompt = enhanced_prompt.replace(", ,", ",").replace(",,", ",")
    enhanced_prompt = " ".join(enhanced_prompt.split())  # Normalize whitespace
    
    return enhanced_prompt

def create_comparison_report(output_dir):
    """
    Create a comparison report showing original vs enhanced prompts
    """
    print("\n" + "="*80)
    print("PROMPT ENHANCEMENT COMPARISON REPORT")
    print("="*80)
    
    # Load original
    with open('prompts_simple.json', 'r') as f:
        original = json.load(f)
    
    # Load enhanced versions
    enhanced_files = {
        "FlyMy": os.path.join(output_dir, "prompts_mid_flymy.json"),
        "FAL": os.path.join(output_dir, "prompts_mid_fal.json"),
        "OpenAI": os.path.join(output_dir, "prompts_mid_openai.json")
    }
    
    enhanced_configs = {}
    for api_name, file_path in enhanced_files.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                enhanced_configs[api_name] = json.load(f)
    
    # Show examples for each category
    for category_name in original["categories"].keys():
        print(f"\n{category_name.upper()} CATEGORY:")
        print("-" * 40)
        
        # Get first prompt from each intensity level
        for intensity_level in ["intensity_1_subtle", "intensity_2_moderate"]:
            if (intensity_level in original["categories"][category_name] and 
                original["categories"][category_name][intensity_level]):
                
                original_prompt_data = original["categories"][category_name][intensity_level][0]
                original_prompt = original_prompt_data["prompt"]
                prompt_id = original_prompt_data["id"]
                
                print(f"\nPrompt {prompt_id} ({intensity_level}):")
                print(f"Original: {original_prompt}")
                
                for api_name, config in enhanced_configs.items():
                    if (intensity_level in config["categories"][category_name] and
                        config["categories"][category_name][intensity_level]):
                        enhanced_prompt = config["categories"][category_name][intensity_level][0]["prompt"]
                        print(f"{api_name:8}: {enhanced_prompt}")

def main():
    """
    Main function to enhance prompts and create reports
    """
    print("Face Identity Preservation Benchmark - Prompt Enhancement")
    print("=" * 60)
    
    simple_prompts_file = "prompts_simple.json"
    output_dir = "enhanced_prompts"
    
    if not os.path.exists(simple_prompts_file):
        print(f"Error: {simple_prompts_file} not found!")
        print("Please make sure the simple prompts JSON file exists.")
        return
    
    print(f"Input file: {simple_prompts_file}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Enhance prompts for all APIs
    enhance_prompts_for_apis(simple_prompts_file, output_dir)
    
    print(f"\nEnhancement complete! Files saved to: {output_dir}/")
    print("Generated files:")
    print("  - prompts_mid_flymy.json")
    print("  - prompts_mid_fal.json") 
    print("  - prompts_mid_openai.json")
    
    # Create comparison report
    create_comparison_report(output_dir)
    
    print(f"\nNext steps:")
    print(f"1. Review the enhanced prompts in {output_dir}/")
    print(f"2. Test with a few images using the enhanced prompts")
    print(f"3. Use these as input for your generation scripts")
    print(f"4. Run evaluation to compare simple vs mid-level results")

if __name__ == "__main__":
    main()
