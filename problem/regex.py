
from re import *
for i in range(int(input())):
    try:
        print(bool(compile(input())))
    except error:
        print('False')

