import numpy as np

x = int(input())
lis = []
for i in range(x):
    a = int(input())
    lis.append(a)
arr = np.array(lis)
b = arr[::-1]
for i in range(len(b)):
    print(b[i])

