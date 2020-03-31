from itertools import combinations
# string , value = input().upper().split()
# string = sorted(string)
# value= int(value)
# lis = list(combinations(string,value))
# print(lis)
# #lis.sort()
#
# for i in lis:
#     print(i,end='')


string , value  = input().split()

for i in range(1, int(value)+1):
    for j in combinations(sorted(string), i):
        print (''.join(j))