import matplotlib.pyplot as plt
import numpy as np
import random
from math_test import find_longest_element_index
import math
from itertools import chain
from data_smooth import outliers_detect
def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数


def step3():
    file = open('test_list.txt', 'r')
    dataset = [float(x.strip()) for x in file]
    file.close()
    print(dataset)



    t = np.linspace(start = -4, stop = 4, num = len(dataset))

    #y = np.sin(t) + np.random.randn(len(t)) * 0.1
    y=np.array(dataset)
    #print(y)

    a = dataset.copy()



    #===============loop start==============
    for loop_time in range(0,1):
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




        for loop_time_1 in range(0,15):
            start_point_in_original_list = find_longest_element_index(total_list)
            error_detect=0
            try:
                for i in range(0,5):

                    fall_list=round(new_list[i+1][0]-new_list[i][-1])
                    if abs(fall_list)>6 and len(new_list[i+1])<=6 or np.mean(new_list[i+1])>=60 and len(new_list[i+1])>=3:
                        outlier_list=new_list[i+1]
                        makeup_length=len(outlier_list)
                        new_list.remove(outlier_list)


                        for m in range(1,makeup_length+1):
                            makeup_part=new_list[i][-1]
                            new_list[i].append(makeup_part)

                        error_detect=1
                        print("### after this combine, list number is: ",len(new_list))
            except:
                pass
            c = []
            for i in range(0, len(new_list)):
                for m in range(0, len(new_list[i])):
                    c.append(new_list[i][m])


            plt.plot(t, y, "b.-", t, c, "r.-")
            plt.title("loop times: " + str(loop_time_1 + 1))
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.legend(['original data', 'smooth data'])
            plt.grid(True)
            plt.show()

            if loop_time_1!=1 and error_detect==0:
                print("The loop is over!")
                break


        print("new : ",new_list)

        new_list=sum(new_list,[])
        print("total group: ",len(new_list),new_list)







        a=new_list
        #============Loop End============

    #output
    file = open('data_smooth_output.txt', 'w')
    for fp in new_list:
        file.write(str(fp))
        file.write('\n')
    file.close()

step3()