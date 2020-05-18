

def bin_to_gray(num):
    lis = []
    lis.append(int(num[0]))
    for i in range(len(num)-1):
        if int(num[i]) == int(num[i+1]):
            lis.append(0)
        else:
            lis.append(1)
    return lis

print(*bin_to_gray(input("Enter a binary number: ")))