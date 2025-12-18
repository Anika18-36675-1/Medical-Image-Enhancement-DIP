Automated Image Enhancement Pipeline for Medical X-ray Analysis
Introduction
This repository contains the source code and implementation for an automated Digital Image Processing (DIP) pipeline designed for Chest X-ray enhancement. Medical X-rays often suffer from low contrast and noise, which can obscure critical diagnostic features. This project provides a reproducible method to enhance local contrast and fine anatomical details using a sequence of non-linear filters.

We address the common "noise vs. clarity" trade-off by implementing a pipeline that maximizes Entropy (Information Content) while monitoring PSNR (Structural Integrity).
Overall WorkflowThe project follows a specific 4-stage pipeline to ensure that noise is suppressed before sharpening occurs:
Normalization: Pixel intensity standardization.
CLAHE: Local contrast enhancement using an 8 * 8 tile grid.
Median Filter: Non-linear denoising to preserve structural edges.Unsharp 
Masking: Weighted high-frequency detail enhancement (alpha = 0.5).

Technical Methodology
Contrast Enhancement Strategy
A key component of this pipeline is the transition from Global Histogram Equalization (HE) to Contrast Limited Adaptive Histogram Equalization (CLAHE). As shown in the histogram analysis below, CLAHE prevents the over-saturation common in standard HE by redistributing pixel intensities locally.

Pipeline Progression
The effectiveness of each stage is demonstrated in the progression below. Notice how the Median Filter cleans the noise introduced during contrast enhancement, providing a clean input for the final Sharpening stage.

Evaluation & Results
Success is measured through two primary quantitative metrics:
Metric,Original,Enhanced,Impact
Entropy (H),7.410,7.882,Increase: Significant information gain.
PSNR (dB),N/A,24.53,Trade-off: Measured structural penalty.

Discussion of the Trade-off
Our findings demonstrate a measurable Trade-off. The aggressive nature of Unsharp Masking is required to achieve a high Entropy gain (diagnostic clarity), which in turn causes the PSNR to drop below the traditional 30 dB benchmark. This quantification is essential for clinical applications to ensure the balance between visibility and image integrity.

Installation & Usage
Prerequisites
Install the required libraries:
pip install opencv-python numpy matplotlib

Usage
To run the enhancement pipeline:
python main.py --input ./data/sample.png --alpha 0.5

References
Zuiderveld, K. "Contrast Limited Adaptive Histogram Equalization." Graphics Gems IV (1994).

NIH Clinical Center. ChestX-ray14 Database.

Bradski, G. "The OpenCV Library." Dr. Dobb's Journal of Software Tools (2000).
