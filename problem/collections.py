from collections import Counter

# lis = [1,1,2,3,4,5,3,4,2,1,2,3]
# print(Counter(lis))
# print(Counter(lis).items())
# print(Counter(lis).keys())
# print(Counter(lis).values())
num_of_shoes = int(input('num of shoes: '))
all_shoes_size = list(map(int,input().split()))[:num_of_shoes]
num_of_customers = int(input('num of customers: '))
#for i in range(1,num_of_customers+1):
