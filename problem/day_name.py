

from calendar import weekday
mm , dd , yy = map(int,input().split())
day_num = weekday(yy,mm,dd)
print(day_num)
days =["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday", "Sunday"]
print(days[day_num].upper())

