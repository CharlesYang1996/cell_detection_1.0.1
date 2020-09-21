#xu_yang 2020/5/25 cell_detection_1.0.0
#get masked cells image
import cv2 as cv
import matplotlib.pyplot as plt

from pylab import *
from pixelbetweenpoints import pixel_between_two_points

def step1():

    print("============Step 1 Start============")
    #-----read-----
    img=cv.imread("G:\\2020summer\\Project\\Chromophobe_dataset1\\4.jpg")
    img= cv.copyMakeBorder(img,80,300,80,80, cv.BORDER_CONSTANT,value=[255,255,255])
    #img=cv.cvtColor(img,cv.COLOR_BGR2BGRA)

    img_masked=img.copy()
    img_nucleus_white_img=img.copy()

    #-----preprocess-----
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow("gray", gray)

    gauss = cv.GaussianBlur(gray, (5, 5), 5)
    #cv.imshow("gauss1",gauss)

    ret, thresh = cv.threshold(gauss, 190, 255, 0)
    #cv.imshow("thresh",thresh)

    erode = cv.erode(thresh, None, iterations=2)
    #cv.imshow("erode",erode)
    #-----remove outlines-----

    cv.imshow("erode",erode)
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
        if 250 <= cnt_area(cnts[i]) <= 0.8*(img.shape[0]*img.shape[1]):
            counter_number+=1
            #print(cnts[i])
            #print("======")
            cv.drawContours(img_masked, cnts[i], -1, (0, 0, 255), 2) #draw contours
            cv.drawContours(img_nucleus_white_img, [cnts[i]], -1, (255, 255, 255), -1)#masked white
            M = cv.moments(cnts[i])
            try:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv.circle(img_masked, (cX, cY), 3, (255, 255, 255), -1)
                cv.putText(img_masked, str(counter_number), (cX - 20, cY - 20),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                area_of_cells_nucleus.append(cnt_area(cnts[i]))
                location_cells_center[counter_number]=[cX,cY]
            except:
                pass
            if counter_number==6:
                x1=cX
                y1=cY
            if counter_number==7:
                x2=cX
                y2=cY
            if counter_number==1:
                x_sample=cX
                y_sample=cY
            #cv.drawContours(img_masked, [cnts[i]], -1, (255, 255, 255), -1)#mask contours
    #-----put Text-----
    print("total cells number : ", counter_number)

    #cv.line(img_masked, (x1,y1), (x2,y2), (0,0,255), 2)

    list_of_two_points=pixel_between_two_points(x1,x2,y1,y2)
    print(list_of_two_points)

    #-----output information on the line
    height_of_two_points=[]
    height_of_two_points_B=[]
    height_of_two_points_G=[]
    height_of_two_points_R=[]

    for m in range(0,len(list_of_two_points)):
        height = img[list_of_two_points[m][1], list_of_two_points[m][0]]
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
        height_of_two_points.append(height)
    plt.plot(height_of_two_points,color="black")


    plt.show()
    try:
        plt.plot(height_of_two_points_B, color="blue")
        plt.plot(height_of_two_points_G, color="green")
        plt.plot(height_of_two_points_R, color="red")
        plt.savefig("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\Step1_output_2.jpg")
        plt.show()
    except:
        pass



    img_sample=img.copy()
    cv.circle(img_sample, (x_sample, y_sample), 3, (0, 0, 255), -1)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img_sample, "Sample_Point",(x_sample - 20, y_sample - 20),font, 0.7, (255, 255, 255), 2)
    #cv.imshow("img_sample_location_RED_DOT", img_sample)
    print("x_sample = : ",x_sample)#样本标注点的坐标
    print("y_sample = : ",y_sample)

    # save to local
    f = open("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\dict.txt", 'w')
    f.write(str(location_cells_center))
    f.close()
    print("save dict successfully.")

    # < list save
    file1 = open('area_of_nucleus.txt', 'w')
    for fp in area_of_cells_nucleus:
        file1.write(str(fp))
        file1.write('\n')
    file1.close()
    # list save >


    #-----
    cv.imshow('img_copy', img_masked)

    cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp.bmp",img_masked)
    cv.imwrite("G:\\2020summer\\Project\\Cell_classfication_1.0.0\\temp_1.bmp",img_nucleus_white_img)

    #==================================





    print("============Step 1 End============")
    cv.waitKey()

step1()