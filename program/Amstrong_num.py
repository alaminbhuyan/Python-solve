# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
# check a number is amstrong number or not

def check_amstrong_num(num):
    # x = len(num)
    # sum = 0
    # for i in num:
    #     a = pow(int(i),x)
    #     sum+=a

    # if str(sum) == num:
    #     return True
    # else:
    #     return False

    # return True if(str(sum) == num) else False

    # We can only use this code
    return sum(pow(int(i), len(num)) for i in num) == int(num)

result = check_amstrong_num(input("Enter your number: "))
print(result)
