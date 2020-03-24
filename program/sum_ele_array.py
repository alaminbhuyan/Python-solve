from array import array
def Sum_of_arrElement(arr):
    total = 0
    for item in arr:
        total+=item
    return total

a = array('i',[1,2,3])
x = Sum_of_arrElement(a)
print('The sum of array: ',x)

# another way
def Array_sum(Array):
    return sum(Array)

b = array('i',[2,4,6])
print('The sum of array: ',Array_sum(b))