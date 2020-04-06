# import math
# AB = float(input())
# BC = float(input())
#
# print(str(int(round(math.degrees(math.atan2(AB, BC)))))+'°')

from math import degrees,atan2

AB = float(input())
BC = float(input())
result = str(int(round(degrees(atan2(AB, BC)))))+'°'
print(result)