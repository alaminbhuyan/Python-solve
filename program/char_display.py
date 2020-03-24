from string import ascii_lowercase,ascii_uppercase,punctuation

for i in ascii_lowercase:
    print(i,end=" ")
print('')
for i in ascii_uppercase:
    print(i,end=" ")
print('')
for i in punctuation:
    print(i,end=" ")
# another way
print('')
for i in range(97,123):
    print(chr(i),end=" ")
