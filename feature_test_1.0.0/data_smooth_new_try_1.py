import matplotlib.pyplot as plt
import numpy as np

def moving_average(interval, window_size):
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')  # numpy的卷积函数

t = np.linspace(start = -4, stop = 4, num = 72)

file = open('test_list.txt', 'r')
dataset = [float(x.strip()) for x in file]
file.close()
print(dataset)


#y = np.sin(t) + np.random.randn(len(t)) * 0.1
y=np.array(dataset)
print(y)
a = dataset.copy()
mark1 = 0#初始化
mark2 = 0#初始化
total_list=[]
temp_list=[]
for i in range(0,len(a)-1):
    total_list_start_point=0

    temp_list.append(a[i])

    fall=a[i+1]-a[i]
    if abs(fall)>7:
        total_list.append(temp_list)
        temp_list=[]
print(total_list)



y_av = moving_average(interval = y, window_size = 10)
plt.plot(t, y, "b.-", t, a, "r.-")

plt.xlabel('Time')
plt.ylabel('Value')
plt.legend(['original data', 'smooth data'])
plt.grid(True)
plt.show()