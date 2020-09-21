import matplotlib.pyplot as plt
import numpy as np
from math_test import distance
import math
from itertools import chain
from data_smooth import outliers_detect
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数

def Read_list(filename):
    file1 = open(filename+".txt", "r")
    list_row =file1.readlines()
    list_source = []
    for i in range(len(list_row)):
        column_list = list_row[i].strip().split("\t")  # 每一行split后是一个列表
        list_source.append(column_list)                # 在末尾追加到list_source
    for i in range(len(list_source)):  # 行数
        for j in range(len(list_source[i])):  # 列数
            list_source[i][j]=int(list_source[i][j])
    file1.close()
    return list_source


dataset=Read_list('distance_2point_test_list')
print(dataset)
t = np.linspace(start = -4, stop = 4, num = len(dataset))

#y = np.sin(t) + np.random.randn(len(t)) * 0.1
y=np.array(dataset)


a = []
for i in range(0, len(dataset)):

    try:
        x1 = dataset[i][0]
        y1 = dataset[i][1]
        x2 = dataset[i + 1][0]
        y2 = dataset[i + 1][1]
        a.append(distance(x1, y1, x2, y2))
    except:
        x1 = dataset[i][0]
        y1 = dataset[i][1]
        x2 = dataset[0][0]
        y2 = dataset[0][1]
        a.append(distance(x1, y1, x2, y2))
print("a has total : ", len(a)," elements")

for t in range(0,10):

    print(a)

    for i in range(0, len(dataset)):
        try:
            fall = a[i + 1] - a[i]
            if fall>3:
                a[i+1]=min((a[i]+a[i+2])/2,a[i]+2)

                x_old=dataset[i+1][0]
                y_old=dataset[i + 1][1]
                dataset[i+1][0]=0.5*(dataset[i][0]+dataset[i+1][0])
                dataset[i + 1][1] = 0.5 * (dataset[i][1] + dataset[i+1][1])

                x_new=0.5*(dataset[i][0]+dataset[i+1][0])
                y_new=0.5 * (dataset[i][1] + dataset[i+1][1])
                print("one point has fixed! From ",x_old, y_old," to ",x_new, y_new)
                break
            #elif fall<-3:


        except:
            pass

    plt.plot( a, "r.-")

    plt.title("loop times: "+str(t+1))
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend(['original data', 'smooth data'])
    plt.grid(True)
    plt.show()

#============Loop End============

#output
file = open('data_smooth_output.txt', 'w')
for fp in a:
    file.write(str(fp))
    file.write('\n')
file.close()