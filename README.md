# Medical Image Enhancement Using Histogram Equalization and CLAHE
This repository contains the code, sample data, and results for a Digital Image Processing (DIP) project focused on improving the visual quality of medical images—specifically a chest X-ray—using classical enhancement techniques.

The goal is to demonstrate open-science practices, reproducible workflows, and clear documentation for **Assignment 2**.

---

##  1. Project Overview
Medical images such as X-rays often have low contrast or uneven brightness, making subtle anatomical details difficult to see.  
This project enhances a chest X-ray using two classical digital image processing techniques:

- **Histogram Equalization** – global contrast enhancement  
- **CLAHE (Contrast Limited Adaptive Histogram Equalization)** – localized contrast enhancement  

Both methods aim to improve visibility of lung structures, ribs, and soft tissue.

This is an **in-progress version** of the project—final methods will be added later in the course.

---

##  2. Repository Structure


This structure follows open-science guidelines: separation of code, input data, and generated results.

---

##  3. Methods Used

### 🔹 3.1 Histogram Equalization (Global)
- Spreads intensity values across the full range  
- Improves overall brightness and contrast  
- Useful for quickly enhancing low-contrast images  
- **Limitation:** may cause over-brightening or unnatural appearance

### 🔹 3.2 CLAHE (Local Adaptive Enhancement)
- Applies contrast enhancement in small tiles  
- Prevents over-amplification of noise (contrast-limiting step)  
- Better preserves local details in medical images  
- **More suitable for X-rays** because it balances detail and brightness

---

##  4. Code Explanation (`src/main.py`)

The script performs four major steps:

import cv2
import numpy as np
image = cv2.imread("data/sample_image.png", 0)
equalized = cv2.equalizeHist(image)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_output = clahe.apply(image)
cv2.imwrite("results/equalized.png", equalized)
cv2.imwrite("results/clahe.png", clahe_output)
5. Visual Results
🔸 Input Image

data/sample_image.png

🔸 Output 1 — Histogram Equalization

results/equalized.png

🔸 Output 2 — CLAHE

results/clahe.png

Observation:

Histogram Equalization improves global contrast but can appear harsh.

CLAHE produces more balanced and clinically useful enhancement by focusing on local image regions.
 6. Comparison
Method	Type	Strengths	Weaknesses
Histogram Equalization	Global	Fast, boosts overall contrast	Over-enhancement risk
CLAHE	Local	Preserves subtle details, prevents noise	Slower, requires parameter tuning
7. How to Run the Code
Install required libraries:
py -3.13 -m pip install opencv-python numpy
Run the enhancement script:
py -3.13 src/main.py


Outputs will appear in the results/ folder.
8. Future Work (For Final Project)

Add noise-reduction filters (Gaussian, Median)

Apply sharpening (Laplacian, Unsharp Mask)

Process multiple images

Add quality metrics (PSNR, entropy, SSIM)

Plot histograms before/after enhancement

Expand the dataset
