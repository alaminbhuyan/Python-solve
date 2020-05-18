from numpy import *

# a,b,c = map(int,input().split())
#
# arr1 = zeros([a*b*c], dtype=int)
# arr2 = ones([a*b*c], dtype=int)
# print(arr1.reshape(a,b,c))
# print(arr2.reshape(a,b,c))

nums = tuple(map(int, input().split()))
print (zeros(nums, dtype=int))
print (ones(nums, dtype=int))
