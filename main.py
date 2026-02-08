import cv2
import numpy as np

img = cv2.imread("images/RobloxScreenShot20250525_133332566.png")

new_img = np.zeros(img.shape, dtype='uint8')


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (124,98,55), 1)



# def rotate(img_param, angle):
#     height, width = img.shape[:2]
#     point = (width // 2, height // 2)
#
#     mat = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img_param, mat, (width, height))
#
#
# # img = rotate(img, 90)
#
# def transform(img_param, x, y):
#     mat = np.float32([[1, 0, x], [0, 1, y]])
#     return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))
#
# img = transform(img, 30, 200)

cv2.imshow("Out", new_img)
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