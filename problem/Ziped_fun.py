
a,b = map(int,input().split())

lis = [list(map(float,input().split()))[:a] for _ in range(b)]
x = list(zip(*lis))
for i in x:
    print(sum(i)/len(i))


