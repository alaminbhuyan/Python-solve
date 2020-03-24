Finding the percentage
Dict = {}
# num = int(input('enter num of elements: '))
# for i in range(num):
#     keys = input('Enter your keys: ')
#     values = list(map(float,input('enter your values: ').split()))
#     Dict.update({keys:values})
# #print(Dict)
# for a in Dict.values():
#     total = sum(a)/3
#     Dict.update({keys:total})
# name = input('Enter the name: ')
# print(Dict[name])
n = int(input())
Dictonary = {}
for _ in range(n):
    line = input().split()
    name,mark = line[0],line[1:]
    mark = map(float,mark)
    Dictonary[name] = mark
key = input()
query_mark = Dictonary[key]
total = sum(query_mark)/3
print("%.2f" % total)


