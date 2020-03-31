
# a = list(map(int,input().split()))
# b= list(map(int,input().split()))
#
# lis = tuple((x,y) for x in a for y in b)
# print(lis)

from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
lis=list(product(a,b))
for i in lis:
    print(i,end=' ')