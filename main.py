import cv2
import numpy as np

im = cv2.imread("cube.png")
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 45, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (255,0,0), 3)
print(contours.__len__())
cv2.imshow("",im)
cv2.waitKey(0)
cv2.destroyAllWindows()