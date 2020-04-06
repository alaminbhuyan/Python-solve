n = int(input())
s = list(map(int,input().split()))[:n]
s = set(s)
print(sum(s)/len(s))