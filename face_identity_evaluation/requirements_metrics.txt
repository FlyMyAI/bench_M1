# Core scientific computing and data manipulation
numpy>=1.21.0
pandas>=1.3.0

# Image processing
Pillow>=8.3.0

# Deep learning framework
torch>=2.0.0
torchvision>=0.15.0

# Visualization and plotting
matplotlib>=3.4.0
seaborn>=0.11.0

# Progress bars
tqdm>=4.62.0

# Multi-modal AI models
git+https://github.com/openai/CLIP.git

# Evaluation metrics
torchmetrics>=0.11.0
torch-fidelity>=0.3.0

# Alternative: Install torchmetrics with image extras (includes torch-fidelity)
# torchmetrics[image]>=0.11.0

# System utilities
pathlib2>=2.3.0  # For older Python versions (optional)

# Optional: GPU support for PyTorch
# Visit https://pytorch.org/get-started/locally/ for CUDA-specific installation
# Example for CUDA 11.8:
# torch>=2.0.0+cu118
# torchvision>=0.15.0+cu118

# Development and testing (optional)
# pytest>=6.0.0
# black>=21.0.0

# Note: For the UNPG model to work, you would need additional dependencies
# that are specific to the UNPG codebase (models module, etc.)
# Currently the script uses enhanced dummy features when UNPG is unavailable
