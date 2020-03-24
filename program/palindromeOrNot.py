# Python program to check if the given string is palindrome or not

text = input('Enter your text: ')
text = text.casefold()

if text == text[::-1]:
    print('Yes! The text is palaindrome')
else:
    print('Sorry! The text is not plaindrome')

