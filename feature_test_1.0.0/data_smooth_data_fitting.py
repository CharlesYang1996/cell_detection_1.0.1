from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    x_points = [0, 1, 2, 3, 4, 5]
    y_points = [0, 1, 4, 9, 16, 25]  # 实际函数关系式为：y=x^2

    xnew = np.linspace(min(x_points), max(x_points), 100)  # 新制作100个x值。(等差、list[]形式存储)

    tck = interpolate.splrep(x_points, y_points)
    ynew = interpolate.splev(xnew, tck)  # 通过拟合的曲线，计算每一个输入值。(100个结果，list[]形式存储)

    plt.scatter(x_points[:], y_points[:], 25, "red")  # 绘制散点
    plt.plot(xnew, ynew)  # 绘制拟合曲线图
    plt.show()
    return interpolate.splev(x, tck)


print(f(10))