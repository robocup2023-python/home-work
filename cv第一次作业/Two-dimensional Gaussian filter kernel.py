import numpy as np
import math
import matplotlib.pyplot as plt
import cv2
def create_gaussian_kernel(size,sigma):
    kernel=np.zeros((size,size))
    center=size//2
    constant=1/(2*math.pi*sigma**2)
    for x in range(size):
        for y in range(size):
            kernel[x, y] = constant * math.exp(-((x - center) ** 2 + (y - center) ** 2) / (2 * sigma ** 2))
    kernel/=np.sum(kernel)
    return kernel
size=int(input("size=:"))
sigma=float(input("sigma=:"))
gaussian_kernel = create_gaussian_kernel(size, sigma)
print(gaussian_kernel)
plt.imshow(gaussian_kernel, cmap='viridis', interpolation='nearest')
plt.title('Gaussian Kernel')
plt.colorbar()
plt.show()
gaussian_kernel = cv2.getGaussianKernel(size, sigma)
gaussian_kernel_2d = np.outer(gaussian_kernel, gaussian_kernel)

