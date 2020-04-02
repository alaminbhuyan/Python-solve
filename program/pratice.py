
# def fun1(n):
#     def fun2(m):
#         return m*n
#     return fun2
#
# obj1 = fun1(5)
# obj2 = fun1(5)
#
# print(obj1(2))
# print(obj2(3))
# print(obj1(obj2(4)))
from primePy import primes

print(primes.check(5))
print(primes.check(10))
print(primes.factor(15))
print(primes.factors(15))
print(primes.first(15))
print(primes.upto(15))
print(primes.between(50,100))
print(primes.phi(15))
print(primes.sqrt(5))
print(primes.about())