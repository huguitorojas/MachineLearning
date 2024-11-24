import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow from google.colab.patches

imagen = cv2.imread('imagen.png')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
binario = cv2.adaptiveThreshold(grises, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2_imshow(imagen)
cv2_imshow(grises)
cv2_imshow(binario) 
