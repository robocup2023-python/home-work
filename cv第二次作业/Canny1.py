import cv2
import numpy as np
file_path="/home/robocup/cv/cv第一次作业/v2-58537195d3a7ff6e43fe4d4d30ae1ace_1440w.jpg"
size=(5,5)
sigma=1
low_threshold=75
high_threshold=150
def Canny(file_path,low_threshold, high_threshold,size,sigma):
    image=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    smoothed_image=cv2.GaussianBlur(image,size,sigma)
    sobel_x = cv2.Sobel(smoothed_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(smoothed_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    gradient_direction = np.arctan2(sobel_y, sobel_x)
    cv2.imshow("Gradient Magnitude", gradient_magnitude.astype(np.uint8))
    cv2.imshow("Gradient Direction", gradient_direction.astype(np.uint8))
    non_max_suppress=np.zeros_like(smoothed_image)
    for i in range(gradient_magnitude.shape[0]-1):
        for j in range(gradient_magnitude.shape[1]-1):
            angle=gradient_direction[i,j]
            if (0 <= angle < np.pi/8) or (15*np.pi/8 <= angle <= 2*np.pi):
                q = gradient_magnitude[i, j+1]
                r = gradient_magnitude[i, j-1]
            elif (np.pi/8 <= angle < 3*np.pi/8) or (9*np.pi/8 <= angle < 11*np.pi/8):
                q = gradient_magnitude[i+1, j-1]
                r = gradient_magnitude[i-1, j+1]
            elif (3*np.pi/8 <= angle < 5*np.pi/8) or (11*np.pi/8 <= angle < 13*np.pi/8):
                q = gradient_magnitude[i+1, j]
                r = gradient_magnitude[i-1, j]
            elif (5*np.pi/8 <= angle < 7*np.pi/8) or (13*np.pi/8 <= angle < 15*np.pi/8):
                q = gradient_magnitude[i-1, j-1]
                r = gradient_magnitude[i+1, j+1]
            if gradient_magnitude[i,j]>=q and gradient_magnitude[i,j]>=r:
                non_max_suppress[i,j]=gradient_magnitude[i,j]
    cv2.imshow("non_max_suppress",non_max_suppress)
    edge=np.zeros_like(non_max_suppress)
    low_threshold = low_threshold
    high_threshold = high_threshold
    strong_edge=255
    weak_edge=150
    strong_i, strong_j = np.where(non_max_suppress>= high_threshold)
    weak_i, weak_j = np.where((non_max_suppress<= high_threshold) & (non_max_suppress>= low_threshold))
    edge[strong_i, strong_j] = strong_edge
    edge[weak_i, weak_j] = weak_edge
    return edge
edge=Canny(file_path,low_threshold, high_threshold,size,sigma)
cv2.imshow("Edge",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

