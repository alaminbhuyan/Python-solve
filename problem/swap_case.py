from string import ascii_lowercase
# swap case
txt = "AlaMin BhUyAn"
for i in txt:
    if i in ascii_lowercase:
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")
# another way
print('')
print(txt.swapcase())
