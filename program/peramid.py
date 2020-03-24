# print peramid
# Half-peramid
'''def permid(num):
    for i in range(num+1):
        print(i*'*')

permid(int(input('Enter your num: ')))

def permid2(rows):
    for i in range(rows):
        for j in range(i+1):
            print(j+1,end="")
        print("")

permid2(int(input('Enter your rows number: ')))'''

# Full peramid
def full_pyramid(row):
    #for i in reversed(range(row)):
    for i in range(row):
        print(' '*(row-i-1) + '*'*(2*i+1))

full_pyramid(int(input('Enter your row number: ')))
