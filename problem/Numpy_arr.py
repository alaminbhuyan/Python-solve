
import numpy as np

row , col = map(int,input().split())
lis = [list(map(int,input().split()))[:col] for _ in range(row)]

arr = np.array(lis,dtype=int)
np.set_printoptions(legacy="1.13")
print(arr.mean(axis=1))
print(arr.var(axis=0))
print(arr.std())
