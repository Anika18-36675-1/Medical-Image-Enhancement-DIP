import cv2
import numpy as np

# Load input image in grayscale
# This is a sample X-ray or MRI image for the project
image = cv2.imread("data/sample_image.png", 0)

# Apply Histogram Equalization
# This improves global contrast of the medical image
equalized = cv2.equalizeHist(image)

# Apply CLAHE for local contrast enhancement
# CLAHE prevents over-enhancement in medical imaging
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_output = clahe.apply(image)

# Save results
cv2.imwrite("results/equalized.png", equalized)
cv2.imwrite("results/clahe.png", clahe_output)
