from numpy import *


def arrays(arr):
    arrs = array(arr,dtype=float)
    return arrs[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#arr = array(list(map(int,input().split())), dtype=float)
