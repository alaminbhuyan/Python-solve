
Regex_Pattern = r"\w{3}\W{1}\w{10}\W{1}\w{3}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())