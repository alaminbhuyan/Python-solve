
octal = '24'
i = 0
j = 1
decimalNum = 0

while i<len(octal):
    c = int(octal[i])
    w = c/(8**j)
    decimalNum += w
    i+=1
    j+=1
print(decimalNum)
