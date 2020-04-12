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
    items, quantity = input().split()
    d[items] = d.get(items,0)+int(quantity)

for items,quantity in d.items():
    print(items,quantity)