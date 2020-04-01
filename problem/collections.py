

# num_of_shoes = int(input('num of shoes: '))
# all_shoes_size = list(map(int,input().split()))
# l = Counter(all_shoes_size)
# print(l)
# num_of_customers = int(input('num of customers: '))
#for i in range(1,num_of_customers+1):
#print('hello world')
from _collections import Counter
lis = [1,2,1,3,4,2,2,3,3]
print(list(Counter(lis)))