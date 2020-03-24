
# l = [1,2,3]
# print(isinstance(l,list))

def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

print(flatten([1, 2, [3], [4, [5, 6]]]))

print('----------------------------------------------------------------')

from functools import reduce
from operator import concat
List = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
Flat_list = reduce(concat,List)
print(Flat_list)
print('-----------------------------------------------------------------')
Flat_list2 = reduce(lambda x,y:x+y,List)
print(Flat_list2)
print('-----------------------------------------------------------------')
from itertools import chain
li = [[14], [215, 383, 87], [298], [374], [2, 3, 4, 5, 6, 7]]
Flat_list3 = list(chain.from_iterable(li))
print(Flat_list3)
print('-----------------------------------------------------------------')
Flat_list4 = [item for sublist in li for item in sublist]
print(Flat_list4)
print('-----------------------------------------------------------------')
from numpy import concatenate
Flat_list5 = list(concatenate(li).flat)
print(Flat_list5)