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
from itertools import combinations_with_replacement
l = [1,2,3]
for i in combinations_with_replacement(l,3):
    print(i)