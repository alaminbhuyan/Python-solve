#Create a Python Program to get the ASCII value of a given character.

# Char = input('Enter your Char: ')
# print(ord(Char))
from string import ascii_lowercase,ascii_uppercase,ascii_letters

for i in ascii_lowercase:
    print(ord(i),end=' ')

print('')

for i in ascii_uppercase:
    print(ord(i),end=' ')

print('')
print(ascii_letters)

print(ascii_lowercase)
print(ascii_uppercase)

txt = "AlaMin BhUyAn"
for i in txt:
    if i in ascii_lowercase:
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")