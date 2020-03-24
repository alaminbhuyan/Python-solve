from calendar import isleap

year = int(input('Enter your year: '))

if isleap(year):
    print('True')
else:
    print('False')