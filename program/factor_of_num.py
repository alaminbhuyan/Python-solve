# Find the factor of number

def factor_num(num):

    for i in range(1,num+1):
        if num%i == 0:
            print(i)

factor_num(int(input('Enter your number: ')))