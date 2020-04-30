
import numpy as np

row,column = map(int,input().split())

arr = np.array([list(map(int,input().split()))[:column] for _ in range(row)],dtype=int)

x = np.min(arr,axis=1).max()
print(x)