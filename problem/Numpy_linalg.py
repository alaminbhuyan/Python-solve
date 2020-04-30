
import numpy as np

n = int(input())
arr = np.array([list(map(float,input().split()))[:n]for _ in range(n)])
np.set_printoptions(legacy='1.13')
print(round(np.linalg.det(arr)))



#print(round(np.linalg.det(np.array([input().split() for _ in range(int(input()))],float)),2))