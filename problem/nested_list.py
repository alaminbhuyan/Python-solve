#[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# List = []
# for _ in range(int(input())):
#     List.append([input(),float(input())])
# List.sort()
# for i in List:
#     for j in i[1]:
#
#
# print(List)


# n = int(input())
# marksheet = [[input(), float(input())] for _ in range(n)]
# print(marksheet)

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

print(second_highest)
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

