import cv2
import numpy as np

photo = np.zeros((300,450, 3), dtype='uint8')

#RGB
#BGR
# photo[130:170, 220:230] = 255, 0, 0

cv2.rectangle(photo, (100, 0), (200,100), (255,0,0), thickness=3)

cv2.line(photo, (0, photo.shape[0] // 2), (100, photo.shape[0] // 2), (255, 0, 0), thickness=2)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (255, 0, 0), thickness=cv2.FILLED)

cv2.putText(photo, 'printTExt', (50, 150), cv2.FONT_ITALIC, 1, (0, 255, 0), thickness=3)

cv2.imshow('photo', photo)
cv2.waitKey(0)
