# initializing list
test_list = [['24'], ['45'], ['78'], ['40']]

# printing original list
print("The original list : " + str(test_list))
# using list comprehension
# converting string list to integer list
res = [[int(a) for a in sub] for a in test_list for sub in a]
# using map+list
res2 = [list(map(int, list(sub[0]))) for sub in test_list if sub ]

print("The list after conversion : " ,res)
print("The list after conversion : " ,res2)
print('----------------------------------')
#Convert numeric String to integers in mixed List
test_list2 = ["gfg", "1", "is", "6", "best"]

# printing original list
print("The original list : " + str(test_list2))

res3 = [int(element) if element.isdigit() else element for element in test_list2]
res4 = list(map(lambda ele: int(ele) if ele.isdigit() else ele,test_list2))
print("The list after conversion : " ,res3)
print("The list after conversion : " ,res4)
