#Create a circle around the nucleus and walk through all the rays coming from the center, looking for the cell wall
#Xu_Yang 2020.8.11

import math_test
import cv2 as cv
from math_test import *
from pylab import *

from pixelbetweenpoints import pixel_between_two_points

display=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp.jpg")
cv.imshow("location_original", display)

img=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.jpg")
img_result=img.copy()
#img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

cv.imshow("img", img)
#-----preprocess-----
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("gray", gray)

gauss = cv.GaussianBlur(gray, (5, 5), 5)

#cv.imshow("gauss1",gauss)
#print("gauss_test: ",gauss[361][616])
'''
x_sample = :  616
y_sample = :  361
'''
img_shape=gauss.shape
print(img_shape[0],img_shape[1])

# read from local
f = open("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\dict.txt", 'r')
dict_ = eval(f.read())
f.close()
print("read from local : ", dict_)
# distance from single point to center


distance_from_single_point_to_center_list=[]
for m in range(6,7):#对某些点进行测试# 28上一次测试的


    x_sample = dict_[m][0]
    y_sample = dict_[m][1]
    angle_temp_list = angle_round(x_sample, y_sample, 65)  # 第三个参数为圆的半径



    for i in range(1,73):
        x1=angle_temp_list[i-1][0]
        y1 = angle_temp_list[i - 1][1]
        cx=x_sample
        cy=y_sample
        temp_list=pixel_between_two_points(cx,round(x1),cy,round(y1))

        ray_lenth = 0
        compare_distance_value=0
        compare_color_value=255
        color_hist=[]
        #单条射线的所有点，颜色深度的集合，找出前三名
        color_deep_rank={}
        for m in range(0,len(temp_list)):
            x_temp=temp_list[m][0]
            y_temp=temp_list[m][1]

            single_lenth=cell_wall_ray_lenth(cx,cy,x_temp,y_temp)

            color_deep_rank[y_temp, x_temp] = gauss[y_temp][x_temp]

            sorted_color_deep_rank = sorted(color_deep_rank.items(), key=lambda kv: (kv[1], kv[0]), reverse=False)

            if gauss[y_temp][x_temp] <= compare_color_value:
                compare_color_value =gauss[y_temp][x_temp]
                compare_distance_valuevalue=single_lenth

                x_final=x_temp
                y_final=y_temp
            else:
                pass
            #==hist graph
            color_hist.append(gauss[y_temp][x_temp])

        #print("**************** test: compare_color_value: ", compare_color_value,"dic rank: ", sorted_color_deep_rank[0],sorted_color_deep_rank[1],sorted_color_deep_rank[2])
        #plt.plot(color_hist, color="black")
        #plt.show()
        cv.circle(img, (round(x_final), round(y_final)), 1, (0, 0, 255), -1)

        #cv.circle(img, (round(sorted_color_deep_rank[1][0][1]), round(sorted_color_deep_rank[1][0][0])), 1, (0, 255, 255), -1)
        #cv.circle(img, (round(sorted_color_deep_rank[2][0][1]), round(sorted_color_deep_rank[2][0][0])), 1, (0, 255, 255), -1)
        #fixed_data_list = un_angle_round(x_sample,y_sample,fixed_data)
        #cv.circle(img, (round(fixed_data_list[i-1][0]), round(fixed_data_list[i-1][1])), 1, (0, 255, 255), -1)
        cv.circle(img, (round(x1), round(y1)), 1, (255, 0, 255), -1) #半径显示

        #distance test and upload
        distance_from_single_point_to_center_list.append(distance(x_final,y_final,cx,cy))
    #<data_clean
    print(distance_from_single_point_to_center_list)


    # data_clean>
    #< list save
    file = open('test_list.txt', 'w')
    for fp in distance_from_single_point_to_center_list:
        file.write(str(fp))
        file.write('\n')
    file.close()
    #list save >
    plt.plot(distance_from_single_point_to_center_list, color="black")
    from k_means_1D import k_means_1d_def
    #temp_list_1=k_means_1d_def(3,30)[2]
    #plt.plot([temp_list_1[0]]*len(a), color="red", linestyle='--')
    #plt.plot([temp_list_1[1]] * len(a), color="red", linestyle='--')

    plt.show()



cv.imshow("img_test_round", img)


from data_smooth_new_try_1_4_1 import data_smooth_open


# input>
for m in range(6,7):
    data_smooth_open()
    # <input
    file1 = open('data_smooth_output.txt', 'r')
    fixed_data = [float(x.strip()) for x in file1]
    file1.close()
    fixed_data_list = un_angle_round(x_sample, y_sample, fixed_data)
    cv.circle(display, (round(fixed_data_list[i - 1][0]), round(fixed_data_list[i - 1][1])), 1, (0, 255, 0), -1)



cv.waitKey()
