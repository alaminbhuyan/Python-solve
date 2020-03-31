# from calendar import weekday
# mm , dd , yy = map(int,input().split())
# day_num = weekday(yy,mm,dd)
# print(day_num)
# days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
# print(days[day_num].upper())

from pyqrcode import *

s = "www.facebook.com"

url = create(s)

url.svg("my.png",scale=8)