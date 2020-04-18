
n = int(input())
rull_of_english_newsp = set(map(int,input().split()))
n2 = int(input())
rull_of_french_newsp = set(map(int,input().split()))

print(len(rull_of_english_newsp.intersection(rull_of_french_newsp)))