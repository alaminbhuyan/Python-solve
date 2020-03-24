'''year = int(input())

if year%4==0:
    if year%100==0:
        if year%400==0:
            print('True')
        else:
            print('False')
    else:
        print('True')
else:
    print('False')'''

'''def leepyear(x):
    if x%4==0:
        if x%100==0:
            if x%400==0:
                print('True')
            else:
                print('False')
        else:
            print('True')
    else:
        print('False')

leepyear(1990)'''


def is_leap(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
               return True
            else:
                return False
        else:
            return True
    else:
       return False


year = int(input())
print(is_leap(year))