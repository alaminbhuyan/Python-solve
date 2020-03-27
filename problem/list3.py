# n = int(input())
# lis = []
# for i in range(n):
#     data = input().split()
#     #if data[0] != "print" or data[0] != "pop" or data[0] != "sort" or data[0] != "reverse":
#     pos = int(data[1])
#     value = int(data[2])
#     if data[0] == "insert":
#         lis.insert(pos,value)
#     if data[0] == "print":
#         print(lis)
#     if data[0]== "remove":
#         lis.remove(value)
#     if data[0]== "append":
#         lis.append(value)
#     if data[0]== "sort":
#         lis.sort()
#     if data[0]== "pop":
#         lis.pop()
#     if data[0]== "reverse":
#         lis.reverse()

lis = []
for _ in range(6):

    data = input('enter value: ').split()
    if data[0] != "print" or  "remove":
        pos = int(data[1])
        value = int(data[2])
    if data[0] == "remove":
        value = int(data[1])
    if data[0]=="insert":
        lis.insert(pos,value)
    if data[0]=="print":
        print(lis)