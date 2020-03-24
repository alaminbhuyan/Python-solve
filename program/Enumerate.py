some_list = ['a','b','c','d']
for counter,value in enumerate(some_list):
    print(counter,value)
    some_list[counter] = 'alamin'
    print(some_list)

my_list = ['apple', 'banana', 'grapes', 'pear']
print(type(my_list))
counter_list = list(enumerate(my_list, 1))
print(type(counter_list))
print(counter_list)

