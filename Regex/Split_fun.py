# import re
# string = "100,000,000.000"
#
# x = re.split(r'[,.]',string)
#
# for i in x:
#     print(i)

regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))