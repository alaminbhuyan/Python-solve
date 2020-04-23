import re

pattern = r'\d{2}\D{1}\d{2}\D{1}\d{3}'

test_patt = input().lower()

print(test_patt)

x = re.search(pattern,test_patt)
print(bool(x))

