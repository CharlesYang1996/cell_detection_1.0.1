import cv2 as cv

from pylab import *
img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\4_1_2.jpg")

cv.imshow("img", img)
# size
sp = img.shape
sz1 = sp[0]  # height(rows) of image
sz2 = sp[1]  # width(colums) of image
sz3 = sp[2]  # the pixels value is made up of three primary colors
#-----preprocess-----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
cv.imshow("gauss1",gauss)


white_count_hist_list=[]
for k in range(0,255):
    white_count=0
    ret, thresh = cv.threshold(gauss, k, 255, 0)

    for i in range(0,sz2):
        for m in range(0,sz1):
            if thresh[m][i]==255:
                white_count+=1

    white_count_hist_list.append(white_count)

plt.plot(white_count_hist_list,color="black")
plt.axvline(200)
plt.xlabel("deeper")
plt.ylabel("numbers of white")

plt.show()

k=220

ret, thresh = cv.threshold(gauss, 0+k, 255, 0)
cv.imshow("thresh", thresh)
erode = cv.erode(thresh, None, iterations=2)
cv.imshow("erode",erode)

cv.waitKey()