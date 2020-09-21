a=[[1,2,3],[99,2],[1,2,3,4],[3,3,3,33.33,3,3],[1],[2],[9,9,9]]
c=[]
for i in range(0,len(a)):
    for m in range(0,len(a[i])):
        c.append(a[i][m])
print(c)


def find_min_length_list(dataset):
    m=999
    for i in dataset:
        if len(i)<=m:
            m=len(i)
            position=dataset.index(i)



for i in range(0,100):
    if i ==15:
        print("out15")
        break
    elif i ==20:
        print("out20")



def find_longest_element_index(list):
    word_len_list = [len(word) for word in list]
    max_word_len = max(word_len_list)
    for word in list:
        if len(word) == max_word_len:
            print("find_longest_element: ",word)
            print("find_longest_element_index:",list.index(word))


c=[1,2,3,4,5,6]
c.remove(c[2])
print(c)
import matplotlib.pyplot as plt

"""  
    Demo of the histogram (hist) function with a few features.  

    In addition to the basic histogram, this demo shows a few optional features:  

        * Setting the number of data bins  
        * The ``normed`` flag, which normalizes bin heights so that the integral of  
          the histogram is 1. The resulting histogram is a probability density.  
        * Setting the face color of the bars  
        * Setting the opacity (alpha value).  

    """
import numpy as np

"""  
    Demo of the histogram (hist) function with a few features.  

    In addition to the basic histogram, this demo shows a few optional features:  

        * Setting the number of data bins  
        * The ``normed`` flag, which normalizes bin heights so that the integral of  
          the histogram is 1. The resulting histogram is a probability density.  
        * Setting the face color of the bars  
        * Setting the opacity (alpha value).  

    """
import numpy as np
import matplotlib.mlab as mlab
