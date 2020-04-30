import numpy as np

n = int(input())

lis = [list(map(int,input().split()))[:n] for _ in range(n)]
lis2 = [list(map(int,input().split()))[:n] for _ in range(n)]

a = np.array(lis,dtype=int)
b = np.array(lis2,dtype=int)

print(np.dot(a,b))
#print(np.cross(a,b))