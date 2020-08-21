import cv2
import numpy as np

ball_color = 'target'

color_dist = {'red': {'Lower': np.array([0, 60, 60]), 'Upper': np.array([6, 255, 255])},
              'blue': {'Lower': np.array([100, 80, 46]), 'Upper': np.array([124, 255, 255])},
              'target1': {'Lower': np.array([125, 43, 46]), 'Upper': np.array([155, 255, 255])},
              'target': {'Lower': np.array([170, 115, 160]), 'Upper': np.array([200, 135, 190])},

              }


#frame=cv2.imread("G:\\2020summer\Project\output_test\\1.jpg")
frame=cv2.imread("G:\\color_example.jpg")
img4=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

gs_frame = cv2.GaussianBlur(frame, (5, 5), 0)                     # 高斯模糊
hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV)                 # 转化成HSV图像
erode_hsv = cv2.erode(hsv, None, iterations=2)                   # 腐蚀 粗的变细
inRange_hsv = cv2.inRange(erode_hsv, color_dist[ball_color]['Lower'], color_dist[ball_color]['Upper'])

cnts = cv2.findContours(inRange_hsv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

c = max(cnts, key=cv2.contourArea)
rect = cv2.minAreaRect(c)
box = cv2.boxPoints(rect)
cv2.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)

cv2.imshow('camera', frame)
cv2.waitKey(1)


cv2.waitKey(0)
cv2.destroyAllWindows()

