from numpy import *

# n,m = map(int,input().split())
#
# row = list(map(int,input().split()))[:n]
# column = list(map(int,input().split()))[:m]
#
# arr = array([row,column])
#
# print(arr.transpose())
# print(arr.flatten())

n, m = map(int, input().split())
arr = array([input().strip().split() for _ in range(n)], int)
print (arr.transpose())
print (arr.flatten())