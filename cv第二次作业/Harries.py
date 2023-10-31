import cv2
import numpy as np

def non_max_suppression(corners, window_size):
    new_corners = []

    for x, y in corners:
        is_max = True
        for i in range(-window_size, window_size + 1):
            for j in range(-window_size, window_size + 1):
                if (x + i, y + j) in corners and corners[(x, y)] < corners[(x + i, y + j)]:
                    is_max = False
                    break
            if not is_max:
                break

        if is_max:
            new_corners.append((x, y))

    return new_corners

file_path = "/home/robocup/cv/cv第二次作业/harris.png"
size = (5, 5)
sigma = 1

def Harris(file_path, size, sigma, window_size):
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    I_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    I_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    k = 0.2
    M = np.zeros(image.shape)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            M11 = np.sum((I_x[i:i+window_size, j:j+window_size])**2)
            M22 = np.sum((I_y[i:i+window_size, j:j+window_size])**2)
            M12 = np.sum(I_x[i:i+window_size, j:j+window_size] * I_y[i:i+window_size, j:j+window_size])
            det = M11 * M22 - M12 ** 2
            trace = M11 + M22
            R = det - k * (trace ** 2)
            M[i, j] = R

    T = 0.0003 * np.max(M)
    corners = {}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if M[i, j] > T:
                corners[(j, i)] = M[i, j]

    nms_corners = non_max_suppression(corners, window_size)

    output = image.copy()
    output_color = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)
    for corner in nms_corners:
        cv2.circle(output_color, corner, 2, (0, 0, 255), -1)
    return output_color

window_size = 3
harris = Harris(file_path, size, sigma, window_size)
cv2.imshow("Harris", harris)
cv2.imwrite("Harris.png", harris)
cv2.waitKey(0)
cv2.destroyAllWindows()

