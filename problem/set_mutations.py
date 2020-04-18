
# m, base_set = input(), set(map(int, input().split()))
# for i in range(0,int(input())):
#     #eval("base_set.{0}({1})".format(input().split()[0], set(map(int, input().split())) ))
#     exec("base_set.{0}({1})".format(input().split()[0], set(map(int, input().split()))))
# print(sum(base_set))

input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split()))
print(sum(map(int, L)))