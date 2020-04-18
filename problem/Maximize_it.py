# l = [2,5,4]
# l2 = [3,7,8,9]
# l3 = [5,5,7,8,9,10]
# y = []
# z = -1
# for i in l:
#     for j in l2:
#         for k in l3:
#             x = (i**2)+(j**2)+(k**2)%1000
#             if x>z:
#                 a,b,c = i,j,k
#                 z = x
#             #print(i,j,k,"->",x)
#             #print(max(y))
#             #print(a,b,c)
# s_max = (a**2)+(b**2)+(c**2)%1000
#
# print(s_max)

# k , m = map(int,input().split())
# l = list(map(int,input().split()))
# l2 = list(map(int,input().split()))
# l3 = list(map(int,input().split()))
# print(l)
# print(l2)
# print(l3)
# y = []
# z = -1
# for i in l:
#     for j in l2:
#         for k in l3:
#             x = (i**2)+(j**2)+(k**2)%1000
#             if x>z:
#                 a,b,c = i,j,k
#                 z = x
# s_max = (a**2)+(b**2)+(c**2) % m
#
# print(s_max)


# sokale bojte hove alamin

from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))

results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))
