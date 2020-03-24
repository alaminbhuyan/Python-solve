# create a Python program to check whether the given sequence is in Arithmetic Progression (A.P.) or not.

def Progression(List):
    if len(List) == 1:
        return True
    else:
        diff = List[1] - List[0]
        for item in range(len(List)-1):
            if not List[item+1] - List[item] == diff:
                return False
        return True

print(Progression([7, 3, -1, -5]))
print(Progression([3, 5, 7, 9, 10])