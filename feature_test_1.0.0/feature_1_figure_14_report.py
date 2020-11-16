#xu_yang 2020/11/15 cell_detection_1.0.0
#For report feature 14, professor wants to represent the result statistically in terms of color depth.
import cv2 as cv
import matplotlib.pyplot as plt
import time
from math_test import area_calculate_from_points
from pylab import *
from pixelbetweenpoints import pixel_between_two_points

import tkinter as tk
from tkinter import filedialog


def step1(findpeaks=None):
    cell_area_hist_list=[]
    print("============Step 1 Start============")
    #-----read-----
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    #img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\4.jpg")
    img = cv.imread(file_path)
    print("Img size: [Width :",img.shape[0],"]","[Height :",img.shape[1],"]")


    img= cv.copyMakeBorder(img,80,450,60,60, cv.BORDER_CONSTANT,value=[255,255,255])
    #img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

    img_masked=img.copy()
    img_nucleus_white_img=img.copy()

    #-----preprocess-----
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow("gray", gray)

    gauss = cv.GaussianBlur(gray, (5, 5), 5)
    #cv.imshow("gauss1",gauss)

    ret, thresh = cv.threshold(gauss, 140, 255, 0)#正常图数值140，癌症图190
    cv.imwrite("G:\\2020summer\\Project\\Chromophobe_dataset1\\figure3_left.jpg",thresh)
    #cv.imshow("thresh",thresh)

    erode = cv.erode(thresh, None, iterations=2)
    #cv.imshow("erode",erode)


    #-----remove outlines-----

    #cv.imshow("erode",erode)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            erode[0][j]=255
    #-----find contours-----
    cnts, hierarchy = cv.findContours(erode.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_NONE)


    def cnt_area(cnt):
      area = cv.contourArea(cnt)
      return area
    counter_number=0
    location_cells_center={}
    area_of_cells_nucleus=[]
    for i in range(0, len(cnts)):
        if 250 <= cnt_area(cnts[i]) <= 0.2*(img.shape[0]*img.shape[1]):
            cell_area_hist_list.append(cnt_area(cnts[i]))
            #print(cnts[i])
            #cell_area_hist_list.append(area_calculate_from_points(cnts[i]))
            counter_number+=1
            #print(cnts[i])
            #print("======")
            cv.drawContours(img_masked, cnts[i], -1, (0, 0, 255), 2) #draw contours
            cv.drawContours(img_nucleus_white_img, [cnts[i]], -1, (255, 255, 255), -1)#masked white
            M = cv.moments(cnts[i])


            #找出masked细胞内点的坐标



            '''            
            rect = cv.minAreaRect(cnts[i])
            cx, cy = rect[0]
            box = cv.boxPoints(rect)
            box = np.int0(box)
            #cv.drawContours(img_masked, [box], 0, (0, 0, 255), 2)
            #cv.circle(img_masked, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)

            box_gray_color=[]
            for by in range(box[2][1],box[0][1]+1):
                for bx in range(box[1][0],box[3][0]+1):
                    #print(bx,by)
                    #cv.circle(img_masked,(bx, by), 1, (255, 0, 0), 2, 8, 0)
                    box_gray_color.append(gray[bx,by])
            #plt.hist(box_gray_color)

            plt.hist(box_gray_color,bins=50)
            plt.title(str(counter_number))
            #plt.show()

            dist=cv.pointPolygonTest(cnts[i],(50,50),True)

            '''

            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv.circle(img_masked, (cX, cY), 3, (255, 255, 255), -1)
                cv.putText(img_masked, str(counter_number), (cX - 20, cY - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                area_of_cells_nucleus.append(cnt_area(cnts[i]))
                location_cells_center[counter_number]=[cX,cY]
            except:
                pass
            if counter_number==176:
                x1=cX
                y1=cY
            if counter_number==181:
                x2=cX
                y2=cY
            if counter_number==1:
                x_sample=cX
                y_sample=cY
            #cv.drawContours(img_masked, [cnts[i]], -1, (255, 255, 255), -1)#mask contours






    #-----put Text-----
    print("total cells number : ", counter_number)

    cv.line(img_masked, (x1,y1), (x2,y2), (0,0,255), 2)

    list_of_two_points=pixel_between_two_points(x1,x2,y1,y2)
    print(list_of_two_points)

    #-----output information on the line
    height_of_two_points_Gray=[]
    height_of_two_points_B=[]
    height_of_two_points_G=[]
    height_of_two_points_R=[]

    for m in range(0,len(list_of_two_points)):
        height_Gray = gray[list_of_two_points[m][1], list_of_two_points[m][0]]
        try:
            height_B=img[list_of_two_points[m][1],list_of_two_points[m][0]][0]
            height_G = img[list_of_two_points[m][1], list_of_two_points[m][0]][1]
            height_R = img[list_of_two_points[m][1], list_of_two_points[m][0]][2]
            height_of_two_points_B.append(height_B)
            height_of_two_points_G.append(height_G)
            height_of_two_points_R.append(height_R)
        except:
            pass
        #print(height)
        height_of_two_points_Gray.append(height_Gray)
    #plt.plot(height_of_two_points_Gray,color="black")


    #plt.show()
    try:
        plt.title("RGB color between")
        plt.plot(height_of_two_points_B, color="blue")
        plt.plot(height_of_two_points_G, color="green")
        plt.plot(height_of_two_points_R, color="red")
        plt.tick_params(labelsize=13)
        plt.savefig("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\Step1_output_2.jpg")
        plt.show()
        plt.title("gray color between")
        plt.tick_params(labelsize=13)
        plt.plot(height_of_two_points_Gray, color="black")
        plt.show()
    except:
        pass

    import scipy.signal
    #R##################
    plt.title("RGB color between")
    plt.plot(height_of_two_points_B, color="blue")
    plt.plot(height_of_two_points_G, color="green")
    plt.plot(height_of_two_points_R, color="red")


    print('Detect peaks without any filters.')

    height_of_two_points_Gray_reverse=[255-i for i in height_of_two_points_R]


    print('Detect peaks with minimum height and distance filters.')
    indexes, _ = scipy.signal.find_peaks(height_of_two_points_Gray_reverse, height=7, distance=2.1)
    print('Peaks are: %s' % (indexes))
    #clean
    indexes_1=list(indexes)
    indexes_2=[]
    for i in indexes_1:
        if i <0.25*len(height_of_two_points_Gray_reverse) or i >0.75*len(height_of_two_points_Gray_reverse):

            indexes_2.append(i)
            indexes_1.remove(i)
            print(i," is removed")

    print('Peaks fixed are: %s' % (indexes_1))
    if len(indexes_1)!=0:
        temp_list=[abs(i-(len(height_of_two_points_Gray)/2)) for i in indexes_1]

        indexes_1=[indexes_1[temp_list.index(min(temp_list))]]

        #plt.title("gray color between_reverse_marked")
        #plt.plot(height_of_two_points_Gray, color="black")
        plt.plot(indexes_1, [height_of_two_points_R[i] for i in indexes_1], marker="8", markersize=10, color='red',
                 ls="")
        #plt.plot(indexes_2, [height_of_two_points_Gray[i] for i in indexes_2], marker="8", markersize=10, color='green',ls="")

    else:
        print("Warning! Cell boundary detection failed!")

    # G##################
    print('Detect peaks without any filters.')

    height_of_two_points_Gray_reverse = [255 - i for i in height_of_two_points_G]

    print('Detect peaks with minimum height and distance filters.')
    indexes, _ = scipy.signal.find_peaks(height_of_two_points_Gray_reverse, height=7, distance=2.1)
    print('Peaks are: %s' % (indexes))
    # clean
    indexes_1 = list(indexes)
    indexes_2 = []
    for i in indexes_1:
        if i < 0.25 * len(height_of_two_points_Gray_reverse) or i > 0.75 * len(height_of_two_points_Gray_reverse):
            indexes_2.append(i)
            indexes_1.remove(i)
            print(i, " is removed")

    print('Peaks fixed are: %s' % (indexes_1))
    if len(indexes_1) != 0:
        temp_list = [abs(i - (len(height_of_two_points_Gray) / 2)) for i in indexes_1]

        indexes_1 = [indexes_1[temp_list.index(min(temp_list))]]

        #plt.title("gray color between_reverse_marked")
        #plt.plot(height_of_two_points_Gray, color="black")
        plt.plot(indexes_1, [height_of_two_points_G[i] for i in indexes_1], marker="8", markersize=10,
                 color='green',
                 ls="")


    else:
        print("Warning! Cell boundary detection failed!")

    # B##################
    print('Detect peaks without any filters.')

    height_of_two_points_Gray_reverse = [255 - i for i in height_of_two_points_B]

    print('Detect peaks with minimum height and distance filters.')
    indexes, _ = scipy.signal.find_peaks(height_of_two_points_Gray_reverse, height=7, distance=2.1)
    print('Peaks are: %s' % (indexes))
    # clean
    indexes_1 = list(indexes)
    indexes_2 = []
    for i in indexes_1:
        if i < 0.25 * len(height_of_two_points_Gray_reverse) or i > 0.75 * len(height_of_two_points_Gray_reverse):
            indexes_2.append(i)
            indexes_1.remove(i)
            print(i, " is removed")

    print('Peaks fixed are: %s' % (indexes_1))
    if len(indexes_1) != 0:
        temp_list = [abs(i - (len(height_of_two_points_Gray) / 2)) for i in indexes_1]

        indexes_1 = [indexes_1[temp_list.index(min(temp_list))]]

        #plt.title("gray color between_reverse_marked")
        #plt.plot(height_of_two_points_Gray, color="black")
        plt.plot(indexes_1, [height_of_two_points_B[i] for i in indexes_1], marker="8", markersize=10,
                 color='blue',
                 ls="")


    else:
        print("Warning! Cell boundary detection failed!")

    plt.tick_params(labelsize=13)
    plt.show()


    cv.imshow('img_copy', img_masked)


    cv.waitKey()


step1()