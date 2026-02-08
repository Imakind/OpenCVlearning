import cv2
import numpy as np

img = cv2.imread('images/RobloxScreenShot20250525_133332566.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge([b , g, r])

cv2.imshow('out', img)
cv2.waitKey(0)