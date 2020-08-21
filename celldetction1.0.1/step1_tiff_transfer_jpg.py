import os.path

import cv2 as cv

img=cv.imread("G:\s1.jpg")
cv.imshow("img",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
#cv.imshow("gauss1",gauss)


ret, thresh = cv.threshold(gauss, 225, 255, 0)
cv.imshow("thresh",thresh)

dilation = cv.dilate(thresh,(4, 4),iterations = 5)
#cv.imshow("dilation",dilation)


erode = cv.erode(thresh, None, iterations=2)
#cv.imshow("erode",erode)


contours, hierarchy = cv.findContours(gray,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
for i in range(0, len(contours)):
    cv.drawContours(img, contours[i], -1, (255, 0, 0), 2)
cv.imshow("result",img)
cv.waitKey()

