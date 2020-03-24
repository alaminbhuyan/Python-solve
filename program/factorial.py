# Find a factorial of a number

# from math import factorial
# print(factorial(3))

# def Factorials(num):
#     if num>1:
#         return num*Factorials(num-1)
#     else:
#         return 1
#
# print(Factorials(int(input('Enter your number: '))))

def fun(num):
    if num == 0:
        return 1
    else:
        mul = 1
        for i in range(1,num+1):
            mul*=i
        return mul

print('The factorial number is : ',fun(int(input('Enter your number: '))))

fun(3)