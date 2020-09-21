#feature_1
#feature_3
#data_smooth_new_try_1_4_1
#feature_4
import cv2 as cv
from shutil import copyfile
from feature_1 import step1
from feature_3 import step2
from data_smooth_new_try_1_4_3 import step3
from feature_4 import step4




step1()

for i in range(1,89):
    step2(i)
    step3()
    step4(i)
    copyfile("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\ouput_marked.bmp","G:\\2020summer\\Project\\Cell_classfication_1.0.0\\output\\"+str(i)+".bmp")

#display=cv.imread("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.jpg")
#cv.imshow("Final output", display)

#cv.waitKey()
