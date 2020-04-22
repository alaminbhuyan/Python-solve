#
# n = int(input())
#
# def fibonacci(num):
#     lis = [0,1]
#     for i in range(2,num):
#         lis.append(lis[i-2]+lis[i-1])
#     return (lis[0:num])
# x = fibonacci(n)
# print(list(map(lambda x: pow(x,3),x)))

def fibonacci(num):
    lis = [0,1]
    for i in range(2,num):
        lis.append(lis[i-2]+lis[i-1])
    return (lis[0:num])
cube = lambda x: pow(x,3)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))