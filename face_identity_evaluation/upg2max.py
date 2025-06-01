import json
import os
from copy import deepcopy
import random

def create_maximal_prompts(simple_prompts_file, output_dir="maximal_prompts"):
    """
    Create maximally enhanced, complex prompts for different APIs
    
    Args:
        simple_prompts_file: Path to the simple prompts JSON file
        output_dir: Directory to save maximal prompt files
    """
    
    # Load simple prompts
    with open(simple_prompts_file, 'r') as f:
        base_config = json.load(f)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Maximal enhancement strategies for each API
    api_maximal_configs = {
        "flymy": {
            "system_prefix": "Create a hyper-realistic, identity-preserving facial transformation: ",
            "identity_preservation": [
                "maintaining exact facial geometry and bone structure",
                "preserving unique identifying features and characteristics", 
                "keeping distinctive facial proportions and symmetry",
                "retaining original skin undertones and natural complexion",
                "maintaining eye shape, nose structure, and jaw definition"
            ],
            "technical_quality": [
                "ultra-high definition rendering with microscopic detail accuracy",
                "professional studio lighting with perfect shadow gradients",
                "skin texture rendered with pore-level precision and natural aging patterns", 
                "anatomically correct facial muscle movement and tension",
                "photorealistic material properties with accurate subsurface scattering"
            ],
            "environmental": [
                "optimal environmental lighting conditions",
                "controlled atmospheric perspective",
                "professional photography studio setup",
                "balanced color temperature and exposure",
                "seamless background integration"
            ],
            "suffix": "Execute with maximum precision while ensuring complete facial identity preservation throughout the transformation process."
        },
        
        "fal": {
            "system_prefix": "Generate ultra-high-quality, technically precise facial modification: ",
            "identity_preservation": [
                "lock facial landmark coordinates and geometric relationships",
                "preserve biometric identifying features and unique characteristics",
                "maintain facial vector mapping and proportional relationships", 
                "retain distinctive feature signatures and identifying markers",
                "keep original facial topology and structural foundations"
            ],
            "technical_quality": [
                "8K resolution with pixel-perfect detail rendering",
                "advanced neural rendering with state-of-the-art quality",
                "precise algorithmic feature manipulation and transformation",
                "high-fidelity texture synthesis with authentic material properties",
                "cutting-edge AI-driven photorealistic generation technology"
            ],
            "environmental": [
                "optimal computational rendering parameters",
                "advanced lighting simulation algorithms", 
                "professional-grade image synthesis",
                "high-dynamic-range processing",
                "superior quality assurance protocols"
            ],
            "suffix": "Deploy maximum computational resources for optimal results with guaranteed identity consistency."
        },
        
        "openai": {
            "system_prefix": "Create a masterful portrait photograph featuring sophisticated facial modification: ",
            "identity_preservation": [
                "maintaining the subject's inherent facial character and essence",
                "preserving natural human authenticity and individual uniqueness",
                "keeping distinctive personal features and recognizable characteristics",
                "retaining genuine facial expression capacity and natural movement",
                "maintaining realistic human proportions and natural appearance"
            ],
            "technical_quality": [
                "museum-quality portrait photography with exceptional artistic merit",
                "professional photographer expertise with decades of experience",
                "master-level composition and lighting techniques",
                "gallery-worthy aesthetic quality with timeless appeal",
                "award-winning portrait photography standards and execution"
            ],
            "environmental": [
                "sophisticated studio environment with professional equipment",
                "expertly controlled lighting setup with artistic vision",
                "premium photography conditions and atmospheric control",
                "professional backdrop and environmental design",
                "artistic direction with creative excellence"
            ],
            "suffix": "Achieve artistic mastery while maintaining absolute authenticity and natural human beauty."
        }
    }
    
    # Maximal category-specific enhancements
    maximal_category_configs = {
        "emotions": {
            "flymy": {
                "transformation_details": [
                    "precise micro-expression calibration with authentic emotional depth",
                    "accurate facial action unit activation patterns",
                    "natural emotion-driven muscle contraction sequences", 
                    "realistic eye movement and gaze direction adjustments",
                    "authentic lip positioning and mouth shape modifications"
                ],
                "emotional_authenticity": [
                    "genuine emotional resonance and psychological authenticity",
                    "natural emotional progression and facial transition",
                    "believable emotional intensity and expression strength",
                    "authentic human emotional response patterns"
                ],
                "technical_execution": [
                    "frame-by-frame emotional consistency",
                    "smooth emotional transition rendering",
                    "natural facial animation principles"
                ]
            },
            "fal": {
                "transformation_details": [
                    "algorithmic emotion recognition and precise facial mapping",
                    "advanced neural emotion synthesis with high accuracy",
                    "computational emotion modeling with realistic outputs",
                    "AI-driven facial expression generation technology", 
                    "machine learning emotion classification and rendering"
                ],
                "emotional_authenticity": [
                    "data-driven emotional accuracy and validation",
                    "scientifically accurate emotion representation",
                    "psychologically consistent emotional expression patterns",
                    "evidence-based emotional modeling"
                ],
                "technical_execution": [
                    "high-precision emotion rendering algorithms",
                    "advanced computational emotion processing",
                    "optimized neural network emotion synthesis"
                ]
            },
            "openai": {
                "transformation_details": [
                    "masterful emotional storytelling through facial expression",
                    "artistic interpretation of human emotional complexity",
                    "sophisticated emotional nuance and subtle expression",
                    "professional portrait emotion capture techniques",
                    "timeless emotional expression with universal appeal"
                ],
                "emotional_authenticity": [
                    "deeply human emotional connection and relatability",
                    "authentic emotional vulnerability and strength",
                    "genuine human experience and emotional truth",
                    "natural emotional beauty and grace"
                ],
                "technical_execution": [
                    "portrait photography emotional mastery",
                    "artistic emotional direction and guidance", 
                    "creative emotional interpretation"
                ]
            }
        },
        
        "age": {
            "flymy": {
                "transformation_details": [
                    "scientifically accurate aging progression with realistic timeline",
                    "anatomically correct age-related facial changes and development",
                    "natural skin aging patterns with authentic texture evolution",
                    "realistic bone structure maturation and age-appropriate modifications",
                    "accurate hair aging progression with natural color and texture changes"
                ],
                "biological_accuracy": [
                    "medically accurate aging process simulation",
                    "natural collagen and elastin degradation effects",
                    "realistic facial volume changes with age progression",
                    "authentic age-related skin pigmentation adjustments"
                ],
                "technical_execution": [
                    "temporal consistency in aging simulation",
                    "natural aging physics and biological constraints",
                    "realistic age progression algorithms"
                ]
            },
            "fal": {
                "transformation_details": [
                    "advanced age progression algorithms with high precision",
                    "AI-powered aging simulation with temporal accuracy",
                    "computational aging models with scientific validation",
                    "machine learning age transformation with realistic results",
                    "neural network aging synthesis with authentic outputs"
                ],
                "biological_accuracy": [
                    "data-driven aging pattern recognition and application",
                    "statistically accurate aging progression models",
                    "scientifically validated aging transformation algorithms",
                    "evidence-based aging simulation technology"
                ],
                "technical_execution": [
                    "high-fidelity age progression rendering",
                    "advanced temporal modeling algorithms",
                    "optimized aging transformation processing"
                ]
            },
            "openai": {
                "transformation_details": [
                    "artistic interpretation of human aging with dignity and grace",
                    "timeless beauty across all ages with natural elegance",
                    "sophisticated age portrayal with wisdom and character",
                    "masterful age progression with artistic sensitivity",
                    "beautiful aging process with natural human appeal"
                ],
                "biological_accuracy": [
                    "naturally beautiful aging with authentic human charm",
                    "graceful age progression with maintained attractiveness",
                    "dignified aging process with inherent beauty",
                    "authentic human aging with artistic appreciation"
                ],
                "technical_execution": [
                    "portrait photography age mastery",
                    "artistic age interpretation and direction",
                    "creative aging visualization"
                ]
            }
        },
        
        "hair": {
            "flymy": {
                "transformation_details": [
                    "physically accurate hair simulation with realistic dynamics",
                    "authentic hair texture rendering with follicle-level precision",
                    "natural hair movement physics with wind and gravity effects",
                    "realistic hair color gradients with natural highlighting patterns",
                    "accurate hair-scalp interaction and natural growth patterns"
                ],
                "material_properties": [
                    "authentic hair material properties with realistic shine and reflection",
                    "natural hair density variations and realistic volume distribution",
                    "accurate hair strand interaction and natural clumping behavior",
                    "realistic hair aging effects and natural wear patterns"
                ],
                "technical_execution": [
                    "advanced hair rendering algorithms",
                    "realistic hair physics simulation",
                    "natural hair lighting calculations"
                ]
            },
            "fal": {
                "transformation_details": [
                    "cutting-edge hair synthesis technology with neural precision",
                    "AI-driven hair modeling with photorealistic accuracy",
                    "advanced hair generation algorithms with realistic outputs",
                    "machine learning hair transformation with authentic results",
                    "computational hair design with scientific precision"
                ],
                "material_properties": [
                    "algorithmically perfect hair material simulation",
                    "AI-optimized hair texture and color processing",
                    "neural network hair property modeling",
                    "computational hair physics with realistic behavior"
                ],
                "technical_execution": [
                    "high-definition hair rendering systems",
                    "advanced neural hair synthesis",
                    "optimized hair transformation algorithms"
                ]
            },
            "openai": {
                "transformation_details": [
                    "artistic hair styling with fashion-forward creativity",
                    "masterful hair design with aesthetic excellence",
                    "sophisticated hair artistry with professional expertise",
                    "timeless hair beauty with classic and modern appeal",
                    "creative hair interpretation with artistic vision"
                ],
                "material_properties": [
                    "beautifully styled hair with salon-quality perfection",
                    "professionally designed hair with artistic flair",
                    "elegant hair presentation with sophisticated appeal",
                    "stunning hair artistry with creative excellence"
                ],
                "technical_execution": [
                    "professional hair photography mastery",
                    "artistic hair direction and styling",
                    "creative hair visualization"
                ]
            }
        },
        
        "accessories": {
            "flymy": {
                "transformation_details": [
                    "physically accurate accessory integration with realistic physics",
                    "natural accessory-face interaction with authentic contact points",
                    "realistic accessory materials with accurate surface properties",
                    "authentic accessory shadows and reflections with environmental accuracy",
                    "natural accessory wear patterns and realistic aging effects"
                ],
                "integration_quality": [
                    "seamless accessory blending with natural facial features",
                    "realistic accessory positioning with anatomical accuracy",
                    "authentic accessory scale and proportional relationships",
                    "natural accessory comfort and realistic fit appearance"
                ],
                "technical_execution": [
                    "advanced accessory rendering algorithms",
                    "realistic accessory physics simulation",
                    "natural accessory lighting integration"
                ]
            },
            "fal": {
                "transformation_details": [
                    "AI-powered accessory placement with computational precision",
                    "machine learning accessory integration with optimal results",
                    "neural network accessory modeling with realistic accuracy",
                    "algorithmic accessory design with perfect positioning",
                    "computational accessory synthesis with authentic outputs"
                ],
                "integration_quality": [
                    "algorithmically optimized accessory-face harmony",
                    "AI-driven accessory scale and proportion calculations",
                    "neural network accessory blending technology",
                    "computational accessory fit optimization"
                ],
                "technical_execution": [
                    "high-precision accessory rendering systems",
                    "advanced neural accessory synthesis",
                    "optimized accessory integration algorithms"
                ]
            },
            "openai": {
                "transformation_details": [
                    "fashionable accessory styling with contemporary appeal",
                    "artistic accessory selection with aesthetic harmony",
                    "sophisticated accessory design with elegant integration",
                    "timeless accessory beauty with classic sophistication",
                    "creative accessory interpretation with artistic flair"
                ],
                "integration_quality": [
                    "beautifully coordinated accessory ensemble",
                    "professionally styled accessory presentation",
                    "elegantly integrated accessory design",
                    "artistically harmonious accessory composition"
                ],
                "technical_execution": [
                    "professional accessory photography mastery",
                    "artistic accessory direction and styling",
                    "creative accessory visualization"
                ]
            }
        }
    }
    
    # Generate maximal prompts for each API
    for api_name, api_config in api_maximal_configs.items():
        enhanced_config = deepcopy(base_config)
        enhanced_config["benchmark_info"]["name"] = f"Face Identity Preservation Benchmark - Maximal Level ({api_name.upper()})"
        enhanced_config["benchmark_info"]["version"] = f"1.0-maximal-{api_name}"
        
        # Enhance each category
        for category_name, category_data in enhanced_config["categories"].items():
            category_enhancement = maximal_category_configs[category_name][api_name]
            
            # Enhance prompts in each intensity level
            for intensity_level in ["intensity_1_subtle", "intensity_2_moderate", "intensity_3_intense"]:
                if intensity_level in category_data and category_data[intensity_level]:
                    for prompt_data in category_data[intensity_level]:
                        original_prompt = prompt_data["prompt"]
                        
                        # Build maximal enhanced prompt
                        maximal_prompt = create_maximal_prompt(
                            original_prompt,
                            api_config,
                            category_enhancement,
                            prompt_data["expected_difficulty"]
                        )
                        
                        prompt_data["prompt"] = maximal_prompt
                        prompt_data["enhancement_level"] = "maximal"
                        prompt_data["api_optimized"] = api_name
                        prompt_data["complexity_score"] = calculate_complexity_score(maximal_prompt)
        
        # Save maximal prompts for this API
        output_file = os.path.join(output_dir, f"prompts_maximal_{api_name}.json")
        with open(output_file, 'w') as f:
            json.dump(enhanced_config, f, indent=2)
        
        print(f"Maximal prompts for {api_name.upper()} saved to: {output_file}")

def create_maximal_prompt(original_prompt, api_config, category_enhancement, difficulty):
    """
    Create maximally enhanced prompt with all possible enhancements
    """
    
    # Determine enhancement intensity based on difficulty
    enhancement_intensity = {
        "easy": {"transform": 2, "auth": 1, "tech": 2, "identity": 2, "env": 1},
        "medium": {"transform": 3, "auth": 2, "tech": 3, "identity": 3, "env": 2}, 
        "hard": {"transform": 4, "auth": 3, "tech": 4, "identity": 4, "env": 3},
        "very_hard": {"transform": 5, "auth": 4, "tech": 5, "identity": 5, "env": 4}
    }
    
    intensity = enhancement_intensity.get(difficulty, enhancement_intensity["medium"])
    
    # Build comprehensive prompt components
    prompt_components = []
    
    # System prefix
    prompt_components.append(api_config["system_prefix"])
    
    # Core transformation (enhanced)
    enhanced_core = f"execute the following transformation with absolute precision: {original_prompt.lower()}"
    prompt_components.append(enhanced_core)
    
    # Add transformation details
    selected_transform = random.sample(
        category_enhancement["transformation_details"], 
        min(intensity["transform"], len(category_enhancement["transformation_details"]))
    )
    prompt_components.extend(selected_transform)
    
    # Add authenticity requirements  
    if "emotional_authenticity" in category_enhancement:
        selected_auth = random.sample(
            category_enhancement["emotional_authenticity"], 
            min(intensity["auth"], len(category_enhancement["emotional_authenticity"]))
        )
        prompt_components.extend(selected_auth)
    elif "biological_accuracy" in category_enhancement:
        selected_auth = random.sample(
            category_enhancement["biological_accuracy"], 
            min(intensity["auth"], len(category_enhancement["biological_accuracy"]))
        )
        prompt_components.extend(selected_auth)
    elif "material_properties" in category_enhancement:
        selected_auth = random.sample(
            category_enhancement["material_properties"], 
            min(intensity["auth"], len(category_enhancement["material_properties"]))
        )
        prompt_components.extend(selected_auth)
    elif "integration_quality" in category_enhancement:
        selected_auth = random.sample(
            category_enhancement["integration_quality"], 
            min(intensity["auth"], len(category_enhancement["integration_quality"]))
        )
        prompt_components.extend(selected_auth)
    
    # Add technical execution
    selected_tech_cat = random.sample(
        category_enhancement["technical_execution"], 
        min(intensity["tech"], len(category_enhancement["technical_execution"]))
    )
    prompt_components.extend(selected_tech_cat)
    
    # Add identity preservation
    selected_identity = random.sample(
        api_config["identity_preservation"], 
        min(intensity["identity"], len(api_config["identity_preservation"]))
    )
    prompt_components.extend(selected_identity)
    
    # Add technical quality
    selected_tech_api = random.sample(
        api_config["technical_quality"], 
        min(intensity["tech"], len(api_config["technical_quality"]))
    )
    prompt_components.extend(selected_tech_api)
    
    # Add environmental factors
    selected_env = random.sample(
        api_config["environmental"], 
        min(intensity["env"], len(api_config["environmental"]))
    )
    prompt_components.extend(selected_env)
    
    # Add suffix
    prompt_components.append(api_config["suffix"])
    
    # Join and clean up
    maximal_prompt = ". ".join(component.strip().rstrip(',').rstrip('.') for component in prompt_components if component.strip())
    maximal_prompt = maximal_prompt.replace(".. ", ". ").replace("..", ".")
    
    return maximal_prompt

def calculate_complexity_score(prompt):
    """Calculate a complexity score for the prompt"""
    word_count = len(prompt.split())
    technical_terms = ["ultra-high", "advanced", "neural", "algorithmic", "professional", "precision", "authentic", "realistic"]
    technical_count = sum(1 for term in technical_terms if term.lower() in prompt.lower())
    
    return {
        "word_count": word_count,
        "technical_terms": technical_count,
        "complexity_rating": min(5, (word_count // 20) + technical_count)
    }

def create_maximal_comparison_report(output_dir):
    """
    Create a comprehensive comparison report
    """
    print("\n" + "="*100)
    print("MAXIMAL PROMPT ENHANCEMENT COMPARISON REPORT")
    print("="*100)
    
    # Load original
    with open('prompts_simple.json', 'r') as f:
        original = json.load(f)
    
    # Load maximal versions
    maximal_files = {
        "FlyMy": os.path.join(output_dir, "prompts_maximal_flymy.json"),
        "FAL": os.path.join(output_dir, "prompts_maximal_fal.json"),
        "OpenAI": os.path.join(output_dir, "prompts_maximal_openai.json")
    }
    
    maximal_configs = {}
    for api_name, file_path in maximal_files.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                maximal_configs[api_name] = json.load(f)
    
    # Show detailed examples
    example_categories = ["emotions", "age"]
    for category_name in example_categories:
        print(f"\n{category_name.upper()} CATEGORY - MAXIMAL ENHANCEMENT:")
        print("-" * 80)
        
        # Get first prompt from subtle intensity
        if ("intensity_1_subtle" in original["categories"][category_name] and 
            original["categories"][category_name]["intensity_1_subtle"]):
            
            original_prompt_data = original["categories"][category_name]["intensity_1_subtle"][0]
            original_prompt = original_prompt_data["prompt"]
            prompt_id = original_prompt_data["id"]
            difficulty = original_prompt_data["expected_difficulty"]
            
            print(f"\nPrompt {prompt_id} ({difficulty} difficulty):")
            print(f"Original: {original_prompt}")
            print()
            
            for api_name, config in maximal_configs.items():
                if ("intensity_1_subtle" in config["categories"][category_name] and
                    config["categories"][category_name]["intensity_1_subtle"]):
                    maximal_prompt_data = config["categories"][category_name]["intensity_1_subtle"][0]
                    maximal_prompt = maximal_prompt_data["prompt"]
                    complexity = maximal_prompt_data.get("complexity_score", {})
                    
                    print(f"{api_name} Maximal ({complexity.get('word_count', 'N/A')} words, "
                          f"complexity: {complexity.get('complexity_rating', 'N/A')}/5):")
                    print(f"{maximal_prompt}")
                    print()

def main():
    """
    Main function to create maximal enhanced prompts
    """
    print("Face Identity Preservation Benchmark - MAXIMAL Prompt Enhancement")
    print("=" * 70)
    
    simple_prompts_file = "prompts_simple.json"
    output_dir = "maximal_prompts"
    
    if not os.path.exists(simple_prompts_file):
        print(f"Error: {simple_prompts_file} not found!")
        print("Please make sure the simple prompts JSON file exists.")
        return
    
    print(f"Input file: {simple_prompts_file}")
    print(f"Output directory: {output_dir}")
    print("Creating MAXIMUM complexity prompts for ultimate API performance...")
    print()
    
    # Create maximal prompts for all APIs
    create_maximal_prompts(simple_prompts_file, output_dir)
    
    print(f"\nMaximal enhancement complete! Files saved to: {output_dir}/")
    print("Generated files:")
    print("  - prompts_maximal_flymy.json")
    print("  - prompts_maximal_fal.json") 
    print("  - prompts_maximal_openai.json")
    
    # Create comparison report
    create_maximal_comparison_report(output_dir)
    
    print(f"\nPrompt Progression Summary:")
    print(f"Level 1: Simple prompts (5-10 words)")
    print(f"Level 2: Mid-level prompts (20-40 words) [created earlier]")
    print(f"Level 3: MAXIMAL prompts (50-150+ words) [just created]")
    
    print(f"\nNext steps:")
    print(f"1. Review the maximal prompts in {output_dir}/")
    print(f"2. Test with a few images to verify API compatibility")
    print(f"3. Run comprehensive benchmark: Simple vs Mid vs Maximal")
    print(f"4. Analyze identity preservation across complexity levels")

if __name__ == "__main__":
    main()
