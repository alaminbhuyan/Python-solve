
x = int(input())
s = input().split()[:x]
s = {int(i) for i in s}

for j in range(int(input())):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     eval('s.{0}({1})'.format(*input().split()+['']))
#
# print(sum(s))