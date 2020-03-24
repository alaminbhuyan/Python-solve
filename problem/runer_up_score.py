
num = int(input())
List = list(map(int,input().split()))[:num]
z = max(List)
while max(List) == z:
    List.remove(max(List))
print(max(List))
