import numpy as np

row , col = map(int,input().split())

#lis = [list(map(int,input().split()))[:col] for _ in range(row)]

arr = np.array([list(map(int,input().split()))[:col] for _ in range(row)])

x = arr.sum(axis=0)
print(x.prod())
#print(np.prod(x))
