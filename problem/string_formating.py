# num = int(input())
# for i in range(1,num+1):
#     print("{dec} {oct} {hex} {bin}".format(dec=i,oct=oct(i),hex=hex(i),bin=bin(i)))
n = int(input())
width = len("{0:b}".format(n))
print(width)
for i in range(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))