# using split() method
a,b,c = input("Enter three value: ").split()
print("The value of a: ",a)
print("The value of b: ",b)
print("The value of c: ",c)
# Using list comprehension

x,y,z = [int(i)for i in input("Enter three value: ").split()]
print("The value of x: ",x)
print("The value of y: ",y)
print("The value of z: ",z)

lis = list(map(int,input().split()))
print(lis)

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = [input(), int(input())]
    lst.append(ele)

print(lst)

