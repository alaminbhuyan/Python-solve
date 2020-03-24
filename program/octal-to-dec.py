
# octal = input('Enter your octal num: ')
#
# print("The decimal number is: ",int(octal,8))

# def OctalToDecimal(num):
#     decimal_value = 0
#     base = 1
#
#     while (num):
#         last_digit = num % 10
#         num = int(num / 10)
#         decimal_value += last_digit * base
#         base = base * 8
#     print("The decimal value is :", decimal_value)
#num = input("Enter an octal number :")

#OctalToDecimal(int(24))
octal = input('Enter your octal number: ')
i=0
j = len(octal)-1
decimalNum = 0
while i<len(octal):
    change_datatype = int(octal[i])
    decimalNum += change_datatype * (pow(8,j))
    i+=1
    j-=1
print("The decimal number is : ",decimalNum)
print('You are successfully!!!')
