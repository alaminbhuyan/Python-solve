# Binary to decimal convert

def bin_to_dec(num):
    decimal = 0
    j = len(num)-1
    for digit in num:
        covnvert = int(digit)
        decimal += covnvert*(pow(2,j))
        j = j-1
    return decimal

x=bin_to_dec('10110')
print(x)