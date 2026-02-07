import cv2
import numpy as np

img = cv2.imread('images/robloxscreenshot20250525_133332566.png')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
img = cv2.GaussianBlur(img, (1, 1), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 200, 200)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

cv2.imshow('roblox', img)

cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3, 50000)
# cap.set(4, 50000)

# while True:
#     success, img = cap.read()
#     cv2.imshow('myvideo', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('x'):
#         break