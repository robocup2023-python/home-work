import cv2
import numpy as np
file_path="/home/robocup/cv/cv第一次作业/v2-58537195d3a7ff6e43fe4d4d30ae1ace_1440w.jpg"
image=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
smoothed_image=cv2.GaussianBlur(image,(5,5),1)
sobel_x = cv2.Sobel(smoothed_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(smoothed_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
gradient_direction = np.arctan2(sobel_y, sobel_x)
cv2.imshow("smoothed_image",smoothed_image)
cv2.imshow("Gradient Magnitude", gradient_magnitude.astype(np.uint8))
low_threshold=50
high_threshold=100
edge=cv2.Canny(smoothed_image,low_threshold,high_threshold)
cv2.imshow("Edge",edge)
cv2.imwrite("Edge.jpg",edge)
cv2.waitKey(0)
cv2.destroyAllWindows