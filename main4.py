import cv2
import numpy as np

photo = cv2.imread('images/RobloxScreenShot20250525_133332566.png')
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (0, 0), 80, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(square)

cv2.imshow('kimg', img)
cv2.waitKey(0)