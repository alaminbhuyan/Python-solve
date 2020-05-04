
# def score_words(words_list):
#     score = 0
#     for word in words_list:
#         num_vowels = 0
#         for letter in word:
#             if letter in 'aeiouy':
#                 num_vowels+=1
#         if num_vowels%2==0:
#             score+=2
#         else:
#             score+=1
#     return score
#
# n = int(input())
# lis = list(map(str,input().split()))[:n]
# print(score_words(lis))

def score_words(words):
    return sum(sum(char in 'aeiouy' for char in word) % 2 or 2 for word in words)