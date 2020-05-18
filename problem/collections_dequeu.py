from collections import deque

lis = deque()

for _ in range(int(input())):
    command = input().split()

    if command[0] == "append":
        lis.append(command[1])
    elif command[0] == "appendleft":
        lis.appendleft(command[1])
    elif command[0] == "pop":
        lis.pop()
    elif command[0] == "popleft":
        lis.popleft()

print(*lis)