
m , n = map(int,input().split())
arr = list(map(int,input().split()))[:m]

set1 = list(map(int,input().split()))[:n]
set1 = set(set1)

set2 = list(map(int,input().split()))[:n]
set2 = set(set2)
happyness = 0
happyness2 = 0
for i in arr:
    if i in set1:
        happyness+=1
    elif i in set2:
        happyness -= 1

print(happyness)