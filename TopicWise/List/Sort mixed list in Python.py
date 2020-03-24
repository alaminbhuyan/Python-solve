# Sort mixed list in Python
def mix_list(num):
    try:
        ele = int(num)
        return (0,ele,'')

    except ValueError:
        return (1,num,'')

lis =  [5,'d',4,'a',9,'c',1,'b']
print("The orginal list is: ",lis)
lis.sort(key=mix_list)

print('After sorting the list: ',lis)
print('--------------------------------')

test_list = ['4', 'gfg', '2', 'best', 'is', '3']

# printing original list
print("The original list : " + str(test_list))

# Sort Mixed List
# using sorted() + key + lambda + isdigit()
res = sorted(test_list, key=lambda ele: (0, int(ele))
if ele.isdigit() else (1, ele))

# printing result
print("List after mixed sorting : " + str(res))
