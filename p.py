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

for t in range(int(input())):
    input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
