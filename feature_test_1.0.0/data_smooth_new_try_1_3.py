import matplotlib.pyplot as plt
import numpy as np
import math
from math_test import *
from itertools import chain
from data_smooth import outliers_detect
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数



file = open('test_list.txt', 'r')
dataset = [float(x.strip()) for x in file]
file.close()
print(dataset)
t = np.linspace(start = -4, stop = 4, num = len(dataset))

#y = np.sin(t) + np.random.randn(len(t)) * 0.1
y=np.array(dataset)
print(y)

a = dataset.copy()



#===============loop start==============
for loop_time in range(0,10):
    print("================= Loop times : ",loop_time+1,"================= ")


    total_list=[]
    temp_list=[]
    for i in range(0,len(a)-1):


        temp_list.append(a[i])

        fall=a[i+1]-a[i]
        if abs(fall)>4:
            total_list.append(temp_list)
            temp_list=[]
        if i == len(a)-2:
            temp_list.append(dataset[-1])
            total_list.append(temp_list)

    print("一共分为 ",len(total_list)," 组",total_list)
    new_list=total_list.copy()



    print("初始化")
    print("old : ",total_list)

    
    i=find_min_length_list(new_list)[0]
    print("min_length_list is :", find_min_length_list(new_list)[1])
    tail = new_list[i-1][-1]
    print("tail is : ",tail)
    try:
        head = new_list[i + 1][0]
        print("head is : ",head)
    except:
        head=new_list[0][0]
        print("out of range, so head is:",head)
    unit_distance = (head - tail) / (len(new_list[i]) + 1)
    for m in range(0, len(new_list[i])):
        new_list[i][m] = unit_distance * (m + 1) + tail


    print("new : ",new_list)
    a=[]
    for u in new_list:
        for i in u:

            a.append(i)


    new_list=sum(new_list,[])
    print("total group: ",len(new_list),new_list)






    y_av = moving_average(interval = y, window_size = 10)
    plt.plot(t, y, "b.-", t, new_list, "r.-")

    plt.title("loop times: "+str(loop_time+1))
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.legend(['original data', 'smooth data'])
    plt.grid(True)
    plt.show()
    if len(total_list)==1:
        print("Warning: No error detected, Loop stop!")
        break


    #============Loop End============

#output
file = open('data_smooth_output.txt', 'w')
for fp in new_list:
    file.write(str(fp))
    file.write('\n')
file.close()