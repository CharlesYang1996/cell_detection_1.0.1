import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\normal_2_1.jpg")
gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
# cv.imshow("gauss1",gauss)

thresh_list=[]
for t in range(0,255):
    temp_counter=0
    ret, thresh = cv.threshold(gauss, t, 255, 0)
    for i in range(img1.shape[0]):
        for m in range(img1.shape[1]):
            if thresh[i][m]==255:
                temp_counter+=1
    thresh_list.append(temp_counter)

plt.plot(range(0,len(thresh_list),1),thresh_list)
#plt.title("Chromophobe cell sample white halo thresh value")
plt.title("Normal cell sample white halo thresh value")
plt.show()
