# txt = input()
# pos, value = input().split(' ')
# pos2 = int(pos)
#
# txt2 = list(txt)
# txt2[pos2] = value
# txt = ''.join(txt2)
# print(txt)

# txt = input()
# pos, value = input().split(' ')
# pos2 = int(pos)
#
# txt =txt[:pos2]+ value +txt[pos2+1:]
# print(txt)

string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))


# def count_substring(string, sub_string):
#     result = (sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string]))
#     return result
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)