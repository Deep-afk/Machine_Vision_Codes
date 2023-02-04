import cv2
import matplotlib.pyplot as plt

# Open the image
img = cv2.imread('C:/Users/Naman/Downloads/cat.jpg')

# Apply Canny
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
plt.figure()
plt.imsave('C:/Users/Naman/Documents/Machine vision/edge.png', edges, cmap='gray', format='png')
plt.title('Edge Detected Photo')
plt.imshow(edges, cmap='gray')
plt.show()
