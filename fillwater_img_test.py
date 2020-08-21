import cv2 as cv


img=cv.imread("G:\\2020summer\Project\output_test\\water5.jpg")

cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
cv.imshow("gauss1",gauss)


ret, thresh = cv.threshold(gauss, 165, 255, 0)
cv.imshow("thresh",thresh)
cv.waitKey()
