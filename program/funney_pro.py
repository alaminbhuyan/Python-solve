

def convert_into_ascii(txt):
    lis = []
    for i in txt:
        x = ord(i)
        lis.append(x)
    convert_into_char(lis)


def convert_into_char(lis):
    for i in lis:
        print(chr(i),end="")




convert_into_ascii('kere salar pot')

# txt = 'alamin'
# lis = []
# for i in txt:
#     x = ord(i)
#     lis.append(x)
# print(lis)
# for i in lis:
#     print(chr(i),end="")