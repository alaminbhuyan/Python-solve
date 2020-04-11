

# txt = input()
# x = sorted(txt)
# x2 = ''.join(x)
# a,a2,a3,b,b2,b3 = '','','','','',''
# for i in x2:
#     if i.isdigit():
#         a = a+i
#     else:
#         b = b+i
# for i in a:
#     if int(i)%2==0:
#         a2 = a2 + str(i)
#     else:
#         a3 = a3 + str(i)
# dig = a3 + a2
# for i in b:
#     if i.isupper():
#         b2 = b2+i
#     else:
#         b3 = b3+i
# letter = b3+b2
# print(letter+dig)

print(*(sorted(input(), key=lambda x: (x.isdigit(),x.isdigit() and int(x)%2==0,x.isupper(),x.islower(),x))),sep='')
