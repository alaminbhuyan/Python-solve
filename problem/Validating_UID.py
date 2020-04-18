
from re import *

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    print(u)
    try:
        assert search(r'[A-Z]{2}',u)
        assert search(r'\d\d\d',u)
        assert not search(r'[^a-zA-Z0-9]',u)
        assert not search(r'(.)\1',u)
        assert len(u)==10
    except:
        print("Invalid")
    else:
        print("Valid")