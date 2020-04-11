from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt)-dt.strptime(input(), fmt)).total_seconds())))


# from dateutil import parser
#
# for _ in range(int(input())):
#     d1 = parser.parse(input().strip())
#     d2 = parser.parse(input().strip())
#     print(abs(int((d2-d1).total_seconds())))


