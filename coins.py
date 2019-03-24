import matplotlib
import cv2
import sys
import numpy as np

img = cv2.imread('coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

while True:
    cv2.imshow("example", opening)

    key = cv2.waitKey(0)
    if key == 27: #esc key quits out
        cv2.destroyAllWindows()
        break