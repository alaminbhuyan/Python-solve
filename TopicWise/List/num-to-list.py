# Convert a integer number into list

num = 10214564
print('the num {num}'.format(num=num))
lis = [int(x) for x in str(num)]
print('after converthing: {lis}'.format(lis=lis))
# Another way
lis1 = list(map(int,str(num)))
print('The list is : ',lis1)
print(type(lis1[0]))
print('----------------------------------------')
# input from User by one line
lis2 = list(map(int,input('enter your number: ').split()))
print('The list is: ',lis2)
print('-----------------------------------------')
lis3 = ['1','2','3']
lis4 = list(map(int,lis3))
print(lis4)
print(type(lis4[0]))
print('-----------------------------------------')