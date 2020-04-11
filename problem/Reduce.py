
# from functools import reduce
# from fractions import gcd
#
# n = int(input())
# rationals = []
# for i in range(n):
#     rationals.append(list(map(int, input().split())))
# s = [list(a) for a in zip(*rationals)]
# print(s)
# k = [reduce(lambda x, y: x*y, s[i]) for i in range(2)]
# c = reduce(gcd, k)
# for i in range(2):
#     k[i] //= c
# print(*k)

from functools import reduce
from fractions import *
rational = []
for i in range(int(input())):
    rational.append(list(map(int,input().split())))
print(rational)
lis = [[row[i] for row in rational] for i in range(2)]
print(lis)
#l = [list(a) for a in zip(*rational)]

x = [reduce(lambda a,b:a*b,lis[i]) for i in range(2)]
y = Fraction(x[0],x[1])
m,n = y.numerator,y.denominator
print(m,n)



