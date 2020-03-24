# how to remove punctuation in a text
from string import punctuation
text = "hi how';]][[] you';[]] al'[]]'min"
#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
text2 = ""
for char in text:
    if char not in punctuation:
        text2 = text2+char
print(text2)
