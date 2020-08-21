import cv2 as cv
import numpy as np

ball_color = 'purple'

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'green': {'Lower': np.array([35, 43, 35]), 'Upper': np.array([90, 255, 255])},
              'purple': {'Lower': np.array([125,43, 46]), 'Upper': np.array([155, 255, 255])},
               'target': {'Lower': np.array([140, 40, 190]), 'Upper': np.array([160, 80, 220])}
              }


frame=cv.imread("G:\\2020summer\Project\output_test\\1.jpg")
#frame=cv.imread("G:\\color_example.jpg")
img4=cv.cvtColor(frame, cv.COLOR_BGR2RGB)
frame_version_2=frame.copy()
gs_frame = cv.GaussianBlur(frame, (5, 5), 3)                     # 高斯模糊
hsv = cv.cvtColor(gs_frame, cv.COLOR_BGR2HSV)                 # 转化成HSV图像
#erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
#cv.imshow("123",gs_frame)
inRange_hsv = cv.inRange(hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])
#cv.imshow("1235",inRange_hsv)
cnts, hierarchy = cv.findContours(inRange_hsv.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print("total cells number : ", len(cnts))
for i in range(0, len(cnts)):
    cv.drawContours(frame_version_2, [cnts[i]], -1, (255, 255, 255), -1)

cv.imshow('frame_2', frame_version_2)
cv.imwrite("G:\\2020summer\Project\output_test\\2_output.jpg",frame_version_2)
#---------------insert_circle_detction________

# coding:utf8

img_cicle=frame_version_2.copy()
img_gray = cv.cvtColor(img_cicle, cv.COLOR_BGR2GRAY)
# 低同滤波进行平滑图像
img = img_gray
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.imshow("pre_circle", img)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 120,
                           param1=100,param2=30,
                           minRadius=5, maxRadius=20)
"""
cv2.HoughCircles(image, method, dp,
        minDist, circles, param1, param2,
        minRadius, maxRadius)
参数：
    image:　输入图像　必须是灰度图像
    method:检测方法,常用CV_HOUGH_GRADIENT
    dp:检测内侧圆心的累加器图像的分辨率于输入图像之比的倒数，
        如dp=1，累加器和输入图像具有相同的分辨率，如果dp=2，
        累计器便有输入图像一半那么大的宽度和高度
    minDist: 两个圆心之间的最小距离
    param1: 默认100, 是method方法的参数
        在CV_HOUGH_GRADIENT表示传入canny边缘检测的阈值
    param2： 默认100,method的参数，
        对当前唯一的方法霍夫梯度法cv2.HOUGH_GRADIENT，
        它表示在检测阶段圆心 的累加器阈值，
        它越小，就越可以检测到更多根本不存在的圆，
        而它越大的话，能通过检测的圆就更加接近完美的圆形了
    minRadius:默认值0，圆半径的最小值
    maxRadius:默认值0，圆半径的最大值
返回值：

"""
# 整数化
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # 画出外边圆
    cv.circle(img_cicle, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 画出圆心
    cv.circle(img_cicle, (i[0], i[1]), 2, (0, 0, 255), 3)


cv.imshow("circle", img_cicle)





#---------------step 2---------------
gray = cv.cvtColor(frame_version_2, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)
#cv.imshow("gauss1",gauss)


ret, thresh = cv.threshold(gauss, 170, 255, 0)
#cv.imshow("thresh",thresh)

STEP_1_output=cv.imread("G:\\2020summer\Project\output_test\\1_output.jpg")
cv.imshow('Output2', STEP_1_output)
other_cells_contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
for i in range(0, len(other_cells_contours)):
    if cv.contourArea(other_cells_contours[i])>=70 and cv.contourArea(other_cells_contours[i])<=500:
        cv.drawContours(frame_version_2,other_cells_contours[i],-1,(0,255,255),2)
        cv.drawContours(STEP_1_output, other_cells_contours[i], -1, (0, 255, 255), 2)

cv.imshow('Output1', frame_version_2)
cv.imwrite("G:\\2020summer\Project\output_test\\3_output.jpg",frame_version_2)
cv.imshow('Output3', STEP_1_output)

cv.waitKey()