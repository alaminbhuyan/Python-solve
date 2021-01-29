import numpy as np

row , col = map(int,input().split())

a = np.array([list(map(int,input().split()))[:col] for _ in range(row)],dtype=int)
b = np.array([list(map(int,input().split()))[:col] for _ in range(row)],dtype=int)

print(np.add_towNumber(a, b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.array(np.divide(a,b),int))
#print(np.array(a/b,int))
print(np.mod(a,b))
print(np.power(a,b))