# from fractions import *
# from functools import reduce
#
# #def product(fracs):
#
# if __name__ == '__main__':
#     fracs = [[1,2],[3,4],[5,6]]
#     # for _ in range(int(input())):
#     #     fracs.append(Fraction(*map(int, input().split())))
#     # result = product(fracs)
#     # result = fracs
#     # print(result)
#     # print(*result)
#     frac = Fraction(*map(fracs))
#     print(frac[0])
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
     print(item, quantity)



