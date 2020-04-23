

import operator
# from functools import reduce
# def product(fracs):
#     t = reduce(operator.mul , fracs) # complete this line with a reduce statement
#     return t.numerator, t.denominator


from functools import reduce
from fractions import *

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

# this is my logic

n = int(input())
lis = [list(map(int,input().split())) for _ in range(n)]
print(lis)
lis2 = list(zip(*lis))
print(lis2)
k = [reduce(lambda x , y : x*y,lis2[i]) for i in range(2)]

print(k)
#x = Fraction(k[0],k[1]) # this also work
print(*k)
x = Fraction(*k)
print(x.numerator,x.denominator)
