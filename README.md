# Automated Image Enhancement Pipeline for Medical X-ray Analysis

## 📖 Introduction
Medical X-ray imaging is a primary diagnostic tool, yet raw images frequently suffer from low contrast and inherent noise due to varying exposure levels or patient physiology. Such limitations can obscure subtle but critical anatomical features, such as fine pulmonary vascularity or early-stage nodules.

This repository provides an automated, reproducible **Digital Image Processing (DIP) pipeline** designed to maximize the visibility of diagnostic information. By integrating local contrast stretching with non-linear denoising, we provide a robust solution for medical image pre-processing.

---

## 🛠️ Methodology & Implementation
The pipeline is designed as a sequential flow to ensure that contrast is optimized before noise is handled and edges are sharpened.

### 1. Preprocessing & Normalization
Input images are converted to grayscale and normalized to a standard intensity range. This ensures the mathematical consistency of the subsequent filters across different X-ray datasets.

### 2. Contrast Enhancement (CLAHE)
Unlike standard Global Histogram Equalization (HE), which often causes over-saturation (e.g., making bone structures appear "blown out"), we utilize **Contrast Limited Adaptive Histogram Equalization (CLAHE)**. CLAHE operates on an $8 \times 8$ tile grid, enhancing local contrast while preventing the amplification of background noise.

![Histogram Comparison](./assets/histograms.png)
*Figure 1: Comparison between Original, HE, and CLAHE processed images with corresponding histograms.*

### 3. Non-Linear Denoising (Median Filter)
X-ray data often contains impulsive "salt-and-pepper" noise. We apply a **Median Filter** specifically because it is edge-preserving. It cleans random noisy pixels while maintaining the sharp boundaries of ribs and soft tissues, which is vital for clinical accuracy.

### 4. Controlled Sharpening (Unsharp Masking)
To define fine diagnostic details, we use **Unsharp Masking**. This creates a high-frequency mask that is added back to the image with a weight factor ($\alpha$). We set $\alpha = 0.5$ to balance visual sharpness with image integrity.

![Pipeline Progression](./assets/progression.png)
*Figure 2: Step-by-step visual progression of the enhancement pipeline.*

---

## 📊 Evaluation & Quantitative Analysis
We evaluate the performance of the pipeline using two objective metrics to quantify the "Information vs. Quality" trade-off.

| Metric | Baseline (Original) | Final Enhanced | Goal/Impact |
| :--- | :--- | :--- | :--- |
| **Entropy ($H$)** | 7.410 | **7.882** | **SUCCESS:** Increased information content for diagnosis. |
| **PSNR (dB)** | N/A | **27.53** | **TRADE-OFF:** Quantified cost of aggressive sharpening. |

### The "Trade-Off" Discussion
Our analysis reveals a critical engineering trade-off:
* **Gain:** The increase in **Entropy** proves the pipeline successfully extracted "hidden" diagnostic information from the raw scan.
* **Cost:** The **PSNR of 27.53 dB** (below the standard 30 dB threshold) is the exact quantification of the structural changes introduced by aggressive sharpening. To gain clarity, we accept a measurable sacrifice in structural similarity.

---

## 🚀 Installation & Usage

### 1. Prerequisites
Ensure you have Python 3.8+ installed along with the following libraries:
```bash
pip install opencv-python numpy matplotlib
