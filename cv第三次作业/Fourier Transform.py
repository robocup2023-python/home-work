import cv2
import numpy as np
from scipy.fft import fft2, fftshift, ifftshift, ifft2
image = cv2.imread('/home/robocup/cv/cv第三次作业/截图 2023-11-14 11-33-47.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("Oringinal",image)
image = fft2(image)
image = fftshift(image)
magnitude_spectrum = np.abs(image)
phase_spectrum = np.angle(image)
magnitude_spectrum_normalized1 = cv2.normalize(np.log(1 + magnitude_spectrum), None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('Magnitude Spectrum', magnitude_spectrum_normalized1.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
adjusted_phase_spectrum = (phase_spectrum + np.pi) / (2 * np.pi)
cv2.imshow('Phase Spectrum', adjusted_phase_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols = image.shape
center_row, center_col = rows // 2, cols // 2
radius = 30
mask = np.zeros((rows, cols), dtype=np.uint8)
cv2.circle(mask, (center_col, center_row), radius, 1, thickness=-1)
magnitude_spectrum_masked = magnitude_spectrum * mask
magnitude_spectrum_normalized2 = cv2.normalize(np.log(1 + magnitude_spectrum_masked), None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('mask', magnitude_spectrum_normalized2.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

f_transform_combined = magnitude_spectrum_masked * np.exp(1j * phase_spectrum)
f_transform_combined_shifted = ifftshift(f_transform_combined)
image_combined = ifft2(f_transform_combined_shifted).real
cv2.imshow('Processed', image_combined.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
