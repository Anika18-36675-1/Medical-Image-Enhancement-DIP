# Medical Image Enhancement Using Classical Histogram-Based Techniques

This repository contains a reproducible, open-science implementation of a medical image enhancement pipeline using classical Digital Image Processing (DIP) techniques.  
The current version implements two commonly used contrast-enhancement methods:

- **Histogram Equalization**  
- **CLAHE (Contrast Limited Adaptive Histogram Equalization)**

Although simple, these methods are widely used as preprocessing steps in medical imaging pipelines because they improve visibility of important anatomical details.

This documentation follows the structure and style of the example GitHub project shared by the instructor, providing a clear, transparent explanation of every step and command used.

---

1. Project Motivation

Medical images such as X-rays often suffer from:

- Poor global contrast  
- Uneven illumination  
- Low visibility of subtle anatomical structures  
- Difficulties in distinguishing tissues, ribs, and abnormalities  

Enhancement techniques can improve interpretation by radiologists and can serve as preprocessing for downstream tasks such as:

- Segmentation  
- Classification  
- Image registration  
- Feature extraction  

While modern deep learning methods exist, **classical enhancement is still important** due to:

- Low computational requirements  
- Full interpretability  
- Robustness  
- Ability to improve visibility before applying advanced algorithms  

This project demonstrates how simple, transparent methods can significantly improve X-ray images.

---

2. Repository Structure:
   
### Repository Structure

- **Medical-Image-Enhancement-DIP/**
  - **data/**
    - `sample_image.png` — Original chest X-ray
  - **results/**
    - `equalized.png` — Histogram Equalization output
    - `clahe.png` — CLAHE enhancement output
  - **src/**
    - `main.py` — Image enhancement pipeline
  - **README.md** — Project documentation


This folder structure reflects open, reproducible research practices—clean separation of data, code, and results.

---

3. Enhancement Methods

## 3.1 Histogram Equalization (Global Enhancement)

Histogram Equalization adjusts pixel intensities so that they spread across the entire available range.  
This produces:

- Stronger global contrast  
- Better visibility of bones and lung boundaries  
- Brighter overall appearance  

**Limitation:**  
It may over-enhance bright regions and does not account for local differences in illumination.

---

3.2 CLAHE (Local Adaptive Enhancement)

CLAHE divides the image into tiles (e.g., 8×8), applies histogram equalization to each tile, and then blends them smoothly.  
It also limits contrast amplification to prevent noise from exploding.

**Benefits for medical images:**

- Enhances local soft-tissue contrast  
- Preserves subtle structural details  
- Avoids harsh brightness jumps  
- Handles uneven illumination well  

This makes CLAHE more clinically suitable for X-rays than global histogram equalization.

---

4. Code Explanation (Line-by-Line Breakdown)

Below is the **full explanation of each command used in `main.py`**, written in the style of your professor’s example repo.

✔ Importing Required Libraries
python
import cv2
import numpy as np

cv2 is OpenCV, the core image-processing library.
numpy handles arrays and pixel-level operations.

Loading the Input Image:
image = cv2.imread("data/sample_image.png", 0)

*Loads the X-ray from the data/ folder.
*The 0 flag ensures grayscale mode (correct for X-ray analysis).
*The image is loaded as a NumPy array.

Why grayscale?
Medical X-rays are single-channel intensity images.
Histogram-based enhancement works directly on grayscale matrices.

✔ Applying Global Histogram Equalization
equalized = cv2.equalizeHist(image)

*This performs a global redistribution of pixel intensities.
*Improves visibility of high-density structures
*Makes the entire image brighter
*Enhances overall contrast

Equivalent conceptual command:
Enhanced_Image = HistogramEqualize(Input_Image)

✔ Applying CLAHE (Local Adaptive Enhancement)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_output = clahe.apply(image)
This command:
*Creates a CLAHE processor with chosen parameters:
*clipLimit = 2.0 prevents noise from over-amplifying
*tileGridSize = (8,8) means enhancement is applied tile-by-tile

Applies CLAHE to the input X-ray using:
Output = CLAHE_Processor.apply(Input)
This produces more balanced, diagnostic-quality contrast.

✔ Saving Results
cv2.imwrite("results/equalized.png", equalized)
cv2.imwrite("results/clahe.png", clahe_output)

*These commands export both processed images into the results/ folder.
*This ensures that the enhancement is reproducible and that results are easy to compare.

Equivalent conceptual command:
SaveImage("results/equalized.png", Enhanced_Hist)
SaveImage("results/clahe.png", Enhanced_CLAHE)

✔ Confirmation Message
print("Processing complete. Outputs saved in the 'results' folder.")
Prints a simple message to inform the user that the processing is done.

5. Visual Results
🔸 Original Image
data/sample_image.png

🔸 Global Histogram Equalization
results/equalized.png

🔸 CLAHE (Localized Enhancement)
results/clahe.png

Interpretation:
*Histogram Equalization brightens the image globally.
*CLAHE reveals finer structural details (lung textures, soft tissues).
*CLAHE avoids over-enhancement and produces more clinically meaningful contrast.

| Technique              | Type   | Strengths                                | Weaknesses                |
| ---------------------- | ------ | ---------------------------------------- | ------------------------- |
| Histogram Equalization | Global | Fast, strong contrast enhancement        | Over-enhancement risk     |
| CLAHE                  | Local  | Enhances subtle details, preserves noise | Requires parameter tuning |

How to Run the Code:
Install dependencies:
py -3.13 -m pip install opencv-python numpy

Run the script:
py -3.13 src/main.py

The script will generate:
results/equalized.png
results/clahe.png

9.limitations:
  - Only supports single-image processing
  - No quantitative evaluation metrics (PSNR, SSIM, entropy)
  - No noise filtering implemented
  - No batch/multi-image processing
  - Enhancement parameters not optimized

10.future_work:
  - Add noise reduction filters (Median, Gaussian)
  - Add sharpening (Laplacian, Unsharp Mask)
  - Add histogram visualization (before/after)
  - Add batch image processing support
  - Integrate quality metrics (PSNR, SSIM)
