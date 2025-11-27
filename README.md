# Medical Image Enhancement Using Histogram Equalization and Filtering Techniques

This repository contains the source code and sample data for my Digital Image Processing (DIP) project.  
The goal of the project is to improve the visual quality of medical images (X-ray / MRI) by using classical image enhancement techniques such as Histogram Equalization (HE), CLAHE, Gaussian filtering, Median filtering, and sharpening methods.

---

## Project Description

Medical images often suffer from low contrast, blurring, and noise, which affects clinical interpretation.  
This project applies simple but effective digital image processing methods including:

- Histogram Equalization (global contrast enhancement)  
- CLAHE (local contrast enhancement)  
- Gaussian and Median filtering (noise reduction)  
- Laplacian / Unsharp Mask (sharpening)

These techniques help improve visibility of anatomical structures in medical images.

---

## Repository Structure

---

##  How to Run the Code

### **1. Install Required Libraries**
Make sure Python 3.x is installed.  
Then install dependencies:

### **2. Run the Script**
Inside the `src` directory:

### **3. Output**
Enhanced images will be saved automatically in the `results/` folder:

- `equalized.png`
- `clahe.png`

---

## Sample Data

A sample medical image is included in the `data/` folder:

If additional raw datasets are too large (e.g., NIH ChestX-ray14 or Brain MRI Dataset),  
they will be stored externally on Google Drive or OneDrive and linked here later.

---

## Code Documentation

The source code (`src/main.py`) includes comments explaining:

- What each enhancement method does  
- Why it is used  
- Expected effect on medical images  

This supports open science principles by ensuring transparency, clarity, and reproducibility.

---

## Purpose of This Repository (Assignment 2 Requirement)

This repository was developed to practice:

- GitHub repository creation  
- Version control using Git  
- Writing meaningful commit messages  
- Raw data management  
- Code commenting and documentation  
- Open-science research workflow  








