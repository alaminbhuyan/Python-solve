
a,b = map(int,input().split())
lis = []

for i in range(a):
    lis.append(list(map(int,input().split()[:b])))
k = int(input())
lis.sort(key=lambda x : x[k])
for i in lis:
    print(*i)
# N, M = map(int, input().split())
# rows = [input() for _ in range(N)]
# print(rows)
# K = int(input())
#
# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)

