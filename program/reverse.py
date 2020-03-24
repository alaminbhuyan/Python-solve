# reverse  a sentence

#sentence = "hi i am alamin bhuyan"
sentence = input('Enter your sentence: ')
word_list = sentence.split()
print(word_list)
#print(word_list[::-1])
rev_list = reversed(word_list)
print(rev_list)
#reversed_list= word_list[::-1]
reversed_sentence = " ".join(rev_list)
print(reversed_sentence)

print('-------------------------------')
sen= input('Enter your sentence: ')
print(" ".join(reversed(sen.split())))
