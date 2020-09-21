# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure(figsize=(16,12))
ax = fig.gca(projection="3d")

img = cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\4_3.bmp")		# 修改图片位置
sp = img.shape
sz1 = sp[0]  # height(rows) of image
sz2 = sp[1]  # width(colums) of image
sz3 = sp[2]  # the pixels value is made up of three primary colors
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (7, 7), 7)
imgd = np.array(img)      # image类 转 numpy

# 准备数据
sp = img.shape
h = int(sp[0])#height(rows) of image
w = int(sp[1])#width(colums) of image
##
x_1 = np.linspace(0, sz2, sz2)
y_1 = np.linspace(0, sz1, sz1)
X_1, Y_1 = np.meshgrid(x_1, y_1)

# -------------------------------- 绘制 3D 图形 --------------------------------

x = np.arange(0,w,1)
y = np.arange(0,h,1)
x,y = np.meshgrid(x,y)
z = imgd
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)  # cmap指color map
'''# 平面 z=4.5 的部分
ax.plot_surface(X_1,
                Y_1,
                Z=X_1*0+208,
                color='g',
                alpha=0.6
               )
##'''
# 自定义z轴
ax.set_zlim(-10, 255)
ax.zaxis.set_major_locator(LinearLocator(10))  # z轴网格线的疏密，刻度的疏密，20表示刻度的个数
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  # 将z的value字符串转为float，保留2位小数

# 设置坐标轴的label和标题
ax.set_xlabel('x', size=15)
ax.set_ylabel('y', size=15)
ax.set_zlabel('z', size=15)
ax.set_title("Chromophobe Cell depth of color", weight='bold', size=20)

# 添加右侧的色卡条
fig.colorbar(surf, shrink=0.6, aspect=8)  # shrink表示整体收缩比例，aspect仅对bar的宽度有影响，aspect值越大，bar越窄
plt.show()
