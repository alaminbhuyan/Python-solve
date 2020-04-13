from itertools import combinations_with_replacement

#s , n= input().upper().split()
#n = int(n)
# x = combinations_with_replacement(s,n)
# for i in x:
#     print("".join(i))

from itertools import combinations_with_replacement

s, k = input().upper().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))