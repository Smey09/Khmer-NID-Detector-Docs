## What Is MPS ?    


**MPS** stands for **Metal Performance Shaders**—Apple’s cutting-edge framework for harnessing GPU power on macOS and iOS.

When working with PyTorch and OCR tasks:

- **MPS = macOS GPU acceleration**

If you see `Using MPS (macOS GPU)`, PyTorch has detected an Apple Silicon GPU (M1/M2/M3) and will run computations on it, unlocking much faster neural network processing compared to the CPU.

This means your OCR (like with EasyOCR) can run dramatically quicker—making large-scale image recognition and text extraction much more efficient.

**Quick Reference:**

| Device | What it Means                      |
|--------|------------------------------------|
| CPU    | Uses your computer’s processor     |
| CUDA   | Uses NVIDIA GPU (Windows/Linux)    |
| MPS    | Uses Apple GPU (macOS M1/M2/M3)    |

**Tip:** If you’re on a Mac with Apple Silicon, enabling MPS can supercharge your machine learning workflows!