lis = []
condition1 = "insert"
condition2 = "append"
condition3 = "pop"
condition4 = "sort"
condition5 = "print"
condition6 = "reverse"
condition7 = "remove"
n = int(input())
for i in range(n):
    l = input().split()

    if l[0]==condition1:
        lis.insert(int(l[1]),int(l[2]))
    elif l[0]==condition2:
        lis.append(int(l[1]))
    elif l[0]==condition3:
        lis.pop()
    elif l[0]==condition4:
        lis.sort()
    elif l[0]==condition5:
        print(lis)
    elif l[0]==condition6:
        lis.reverse()
    elif l[0]==condition7:
        lis.remove(int(l[1]))