# FlyMyAI Benchmarks

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
| | **FlyMy AI M1** | **0.791** | **0.926** | **0.876** | **0.838** | **0.910** | **0.841** | **0.864** |

## Face Identity Preservation Benchmark

### 🎯 Single Number Comparison (Identity Preservation)
| API | Overall Score | Advantage |
|-----|---------------|-----------|
| **FlyMyAI** | **0.917** ⭐ | **+44% vs Bagel/Edit, +135% vs OpenAI** |
| Bagel/Edit | 0.636 | +63% vs OpenAI |
| OpenAI | 0.390 | Baseline |

**Dataset**: 8,832 face transformation pairs from 50 FFHQ images across emotions, age, hair, and accessories transformations.

### Best Performance Per Category (Peak Results)
| Category | FlyMyAI Best | Bagel/Edit Best | OpenAI Best | Category Winner |
|----------|-------------|-----------------|-------------|-----------------|
| **Emotions** | 0.977 (maximal) | 0.907 (simple) | 0.401 (mid) | **FlyMyAI** |
| **Age** | 0.915 (mid) | 0.720 (simple) | 0.404 (mid) | **FlyMyAI** |
| **Hair** | 0.899 (maximal) | 0.845 (simple) | 0.398 (mid) | **FlyMyAI** |
| **Accessories** | 0.930 (mid) | **0.955 (simple)** | 0.402 (mid) | **Bagel/Edit** |

### Critical Finding: Prompt Complexity Impact
| API | Simple → Complex | Trend |
|-----|------------------|--------|
| **FlyMyAI** | 0.903 → 0.929 | **Improves +3%** ⬆️ |
| **Bagel/Edit** | 0.857 → 0.457 | **Degrades -47%** ⬇️ |
| **OpenAI** | 0.385 → 0.383 | Stable (poor) → |

### Key Insights
- **FlyMyAI dominates** 3 out of 4 categories and benefits from complex prompts
- **Bagel/Edit competitive** only in accessories with simple prompts (0.955 vs 0.930)
- **Complex prompting advantage**: Only FlyMyAI improves with detailed instructions
- **Production recommendation**: FlyMyAI for identity-critical face transformations

📁 **Detailed results**: [Face Identity Benchmark](./face_identity_evaluation/)
