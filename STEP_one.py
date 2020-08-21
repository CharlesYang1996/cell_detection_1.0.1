#xu_yang 2020/5/25 cell_detection_1.0.0
import cv2 as cv
from pylab import *
img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\1.jpg")
img_BGR=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img_HSV=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#img_HSV=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
#cv.imshow("gauss1",gauss)


ret, thresh = cv.threshold(gauss, 165, 255, 0)
cv.imshow("thresh",thresh)

dilation = cv.dilate(thresh,(4, 4),iterations = 5)
cv.imshow("dilation",dilation)


erode = cv.erode(thresh, None, iterations=2)
cv.imshow("erode",erode)
#==find contours and draw it
contours_area_list=[]
RGB_color_list_R=[]
RGB_color_list_G=[]
RGB_color_list_B=[]

contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours))
def cnt_area(cnt):
  area = cv.contourArea(cnt)
  return area

#boxplot_outlier_detection
def outlier(list):
    list_1=sorted(list)
    n=len(list_1)
    Q1 = list_1[(round((n+1)/4))-1]
    #Q2 = list_1[(round(2(n+1)/4))-1]
    Q3 = list_1[(round(3*(n + 1) / 4)) - 1]
    IQR = Q3 - Q1
    up_outlier=Q3+1.5*IQR
    down_outlier = Q1 - 1.5 * IQR
    return up_outlier
for i in range(0, len(contours)):

    print(cnt_area(contours[i]))
    if cnt_area(contours[i])>=200 and cnt_area(contours[i]) <=70000:
        contours_area_list.append(round(cnt_area(contours[i])))
        for a in contours[i]:
            x_location=a[0][0]
            y_location=a[0][1]
            print("each point location : ",",",a[0],",",a[0][0],",",a[0][1])
            print("color is : ",img_HSV[y_location][x_location])
            RGB_color_list_R.append(img_HSV[y_location][x_location][0])
            RGB_color_list_G.append(img_HSV[y_location][x_location][1])
            RGB_color_list_B.append(img_HSV[y_location][x_location][2])
        print("draw")
        cv.drawContours(img,contours[i],-1,(0,0,255),2)
    if cnt_area(contours[i])>= 3000 and cnt_area(contours[i])<=70000 : #3000
        cv.drawContours(img, contours[i], -1, (255, 0, 0), 2)
    else:
        print("too small, pass")



print(contours_area_list)
print("HSV: H_ave= ",mean(RGB_color_list_R),",S_ave= ",mean(RGB_color_list_G),",V_ave= ",mean(RGB_color_list_B))
plt.hist(contours_area_list, bins=120,color="black")
plt.show()
plt.hist(RGB_color_list_R, bins=20,color="r")
plt.show()
plt.hist(RGB_color_list_G, bins=20,color="g")
plt.show()
plt.hist(RGB_color_list_B, bins=20,color="skyblue")
plt.show()
print("total cells detected:",len(contours),"     ,  up_outlier = ",outlier(contours_area_list))

cv.imshow("img", img)
STEP_1_output=img.copy()
cv.imwrite("G:\\2020summer\Project\output_test\\1_output.jpg",STEP_1_output)
cv.waitKey()



