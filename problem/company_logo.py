
from collections import Counter

for each in Counter(sorted(input())).most_common(3):
    print(*each)