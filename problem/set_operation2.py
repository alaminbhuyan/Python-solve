
m = int(input())
m2 = list(map(int,input().split()))[:m]
m2 = set(m2)
n = int(input())
n2 = list(map(int,input().split()))[:n]
n2 = set(n2)

diff = m2.symmetric_difference(n2)
for i in sorted(diff):
    print(i)