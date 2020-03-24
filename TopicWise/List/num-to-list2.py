# take value a empty list into another list
# lis = []
# lis.append([input(),int(input())])
# print(lis)
print('--------------------------------')

lis2 = ['alamin',12,'tania',13,'fatema',14]
print(lis2[0])
print(type(lis2[0]))

print(lis2[1])
print(type(lis2[1]))
print('---------------------------------')
l = []
l2 = []
for i in lis2:
    if type(i) == str:
        l.append(i)
    else:
        l2.append(i)
print(l)
print(l2)
print('----------------------------------')
a,b,c,d = int(input()),int(input()),int(input()),int(input())
x = [[x,y,z] for x in range(a+1) for y in range(b+1)for z in range(c+1) if x+y+z!=d]
print(x)