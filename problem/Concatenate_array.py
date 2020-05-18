from numpy import *

n,m,p = map(int,input().split())

arr = array([input().split() for _ in range(n)],int)
arr2 = array([input().split() for _ in range(m)],int)

print(concatenate((arr,arr2)))
