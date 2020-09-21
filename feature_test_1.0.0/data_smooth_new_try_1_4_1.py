import matplotlib.pyplot as plt
import numpy as np
import random
import math
from itertools import chain
from data_smooth import outliers_detect
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


def step3():
    print("============Step 3 Start / Dataset Smoothing============")
    file = open('test_list.txt', 'r')
    dataset = [float(x.strip()) for x in file]
    file.close()
    #print(dataset)
    t = np.linspace(start = -4, stop = 4, num = len(dataset))

    #y = np.sin(t) + np.random.randn(len(t)) * 0.1
    y=np.array(dataset)
    #print(y)

    a = dataset.copy()



    #===============loop start==============
    for loop_time in range(0,73):
        error_detect=0
        #print("================= Loop times : ",loop_time+1,"================= ")

        for i in range(0, len(dataset)):
            try:
                fall = a[i + 1] - a[i]
                if fall>9:
                    a[i+1]=min((a[i]+a[i+2])/2,a[i]+random.uniform(-1, 1))
                    error_detect+=1

                    #a[i+1]=0.5*(a[i]+a[i+2])



                    break
                #elif fall<-3:


            except:
                pass








        y_av = moving_average(interval = y, window_size = 10)


        if error_detect==0:
            print("Warning: No error detected, Loop stop!")
            print("All datase")
            plt.plot(t, y, "b.-", t, a, "r.-")
            plt.title("loop times: " + str(loop_time + 1))
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.legend(['original data', 'smooth data'])
            plt.grid(True)
            plt.show()
            break


        #============Loop End============

    #output


    file = open('data_smooth_output.txt', 'w')
    for fp in a:
        file.write(str(fp))
        file.write('\n')
    file.close()
    print("============Step 3 End / Dataset Smoothed============")
