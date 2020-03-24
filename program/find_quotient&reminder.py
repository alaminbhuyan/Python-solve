# Create a Python program to compute Quotient and reminder of two given numbers.
dividend = int(input('Enter your dividend number: '))
divisor = int(input('Enter your divisor number: '))

quotient = dividend//divisor
reminder = dividend%divisor

print('The quotient is: ',quotient)
print('The reminder is : ',reminder)