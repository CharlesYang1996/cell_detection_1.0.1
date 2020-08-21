
a=[12,15,17,19,20,23,25,28,30,33,34,35,36,37,100000]
print(a)
n=len(a)
b=round((n+1)/4)
print(b)
print(a[b-1])


def outlier(list):
    list_1=sorted(list)
    n=len(list_1)
    Q1 = list_1[(round((n+1)/4))-1]
    #Q2 = list_1[(round(2(n+1)/4))-1]
    Q3 = list_1[(round(3*(n + 1) / 4)) - 1]
    IQR = Q3 - Q1
    up_outlier=Q3+1.5*IQR
    down_outlier = Q1 - 1.5 * IQR
    return up_outlier
print(outlier(a))