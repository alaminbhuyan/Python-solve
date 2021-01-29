from numpy import *

# arry = array([1,2,3,4,5,6])
# arry.shape=(2,3)
# print(arry)
arr2 = array(list(map(int,input().split()[:9])))
print(arr2.reshape(3,3))
