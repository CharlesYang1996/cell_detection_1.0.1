import matplotlib.pyplot as plt
import numpy as np
from math_test import find_longest_element_index
import math
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
#print(y)

a = dataset.copy()



#===============loop start==============
for loop_time in range(0,999):
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


    combine_temp_list = []

    print("初始化")
    print("old : ",total_list)




















    error_detect=0
    for i in range(0,len(new_list)-1):
        new_list_start_point = 0

        fall_list=round(new_list[i+1][0]-new_list[i][-1])
        if abs(fall_list)>6 and len(new_list[i+1])==1:
            error_detect+=1
            #print("This list fall is : ", fall_list)

            tail = new_list[i][-1]
            head = new_list[i + 2][0]
            unit_distance=(head-tail)/(len(new_list[i+1])+1)
            new_list[i+1][0]=unit_distance+tail

            if len(new_list[i]) > len(new_list[i + 2]):
                new_list[i].append(new_list[i + 1][0])
                del new_list[i + 1]
            else:
                new_list[i + 2].insert(0, new_list[i+1][0])
                del new_list[i+1]

            print("temp list:",new_list)
            break
        elif abs(fall_list)>6 and len(new_list[i+1])>1:

            if len(new_list[i])>len(new_list[i+1]):
                if fall_list>0:
                    new_list[i+1][0]=min(0.5*(new_list[i][-1]+new_list[i+1][1]),new_list[i+1][0]+1)
                else:
                    new_list[i + 1][0] =max(0.5 * (new_list[i][-1] + new_list[i + 1][1]),(new_list[i+1][0]-1))

                new_list[i].append(new_list[i+1][0])
                del new_list[i+1][0]
            else:

                if fall_list>0:
                    new_list[i][-1]=max(0.5*(new_list[i][-2]+new_list[i+1][1]),new_list[i][-1]-1)
                else:
                    new_list[i][-1]=min(0.5*(new_list[i][-2]+new_list[i+1][1]),new_list[i][-1]+1)
                new_list[i+1].insert(0, new_list[i][-1])
                del new_list[i][-1]

            error_detect+=1
            #print("This list fall is : ", fall_list)

            tail = new_list[i][-1]
            head = new_list[i + 2][0]
            unit_distance=(head-tail)/(len(new_list[i+1])+1)
            for m in range(0,len(new_list[i+1])):

                new_list[i+1][m]=unit_distance*(m+1)+tail



    print("new : ",new_list)

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
    if error_detect==0:
        print("Warning: No error detected, Loop stop!")
        break
    a=new_list
    #============Loop End============

#output
file = open('data_smooth_output.txt', 'w')
for fp in new_list:
    file.write(str(fp))
    file.write('\n')
file.close()