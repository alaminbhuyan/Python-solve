
import re
# for _ in range(int(input())):
#     if re.match(r'[789]\d{9}$',input()):
#         print('YES')
#     else:
#         print('NO')



[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]