# Octal to Decimal
octal = input('Enter your Octal number: ')

i = 0
while i<len(octal):
    if octal[i] == '.':
        pos = i
        break
    i+=1

position = pos+1
j = 1
decimalNum = 0

while position<len(octal):
    c = int(octal[position])
    w = c/(8**j)
    decimalNum += w
    position+=1
    j+=1

k = 0
l = pos-1
decimalNum2 = 0
while k<pos:
    change_datatype = int(octal[k])
    decimalNum2 += change_datatype * (pow(8, l))
    k += 1
    l -= 1
print("The decimal number is ",decimalNum+decimalNum2)