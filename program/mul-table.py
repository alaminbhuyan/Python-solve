# Multiplication table

def mul_table(num):
    for i in range(1,11):
        print(f'{i} x {num} = {i*num}')

mul_table(int(input('Enter your number: ')))