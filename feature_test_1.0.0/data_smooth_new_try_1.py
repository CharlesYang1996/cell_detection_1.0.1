import matplotlib.pyplot as plt
import numpy as np
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
print(y)

a = dataset.copy()
mark1 = 0#初始化
mark2 = 0#初始化
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

print(total_list,"一共分为 ",len(total_list)," 组")
new_list=total_list.copy()


combine_temp_list = []
mark_1_1 = 0
mark_1_2 = 0
error=0
loop_maker=1
print("初始化")
for i in range(0,len(total_list)-1):
    total_list_start_point = 0



    fall_list=round((np.mean(total_list[i+1])-np.mean(total_list[i])))






    if abs(fall_list)>3 and len(total_list[i+1])<6:
        print("This list fall is : ", fall_list)



        #for m in range(0,len(total_list[i+1])):
            #combine_temp_list.append(total_list[i+1][m])

        if mark_1_1==0 and mark_1_2==0:
            mark_1_1=i+1
            mark_1_2=mark_1_1+1
            counter = len(total_list[i + 1])
            print(counter)

        else:
            mark_1_2=i+1
            counter  =counter+len(total_list[i + 1])
            print(counter)


    else:
        print(mark_1_1,mark_1_2)

        print("###",total_list[mark_1_1 - 1][-1],"counter is ",counter)
        print("###", total_list[mark_1_2 + 1][0], "counter is ", counter)

        for n in range(0,counter):
            combine_temp_list.append(round((total_list[mark_1_1 - 1][-1]+((( total_list[mark_1_2 + 1][0]-total_list[mark_1_1 - 1][-1]) / counter)*(n+1)))))
        print(combine_temp_list)
        new_list[mark_1_1+error:mark_1_2+1+error]=[combine_temp_list]
        error = error + mark_1_1 - mark_1_2
        counter=0
        mark_1_1=0
        mark_1_2=0
        loop_maker=1
        combine_temp_list=[]

        print("error is " , error)

print("old : ",total_list)
print("new : ",new_list)

new_list=sum(new_list,[])
print("total group: ",len(new_list),new_list)






y_av = moving_average(interval = y, window_size = 10)
plt.plot(t, y, "b.-", t, new_list, "r.-")


plt.xlabel('Time')
plt.ylabel('Value')
plt.legend(['original data', 'smooth data'])
plt.grid(True)
plt.show()

#output
file = open('test_list.txt', 'w')
for fp in new_list:
    file.write(str(fp))
    file.write('\n')
file.close()