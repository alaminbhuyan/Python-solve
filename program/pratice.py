# def transpose(m):
#     t_matrix = [*zip(*m)]
#     return t_matrix
#
#
#
# print("result=", transpose([[1, 3, 5], [2, 4, 6]]))
# print("result=", transpose([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
# print("result=", transpose([[1, 4, 9]]))

# class myClass:
#     distic = "comilla"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f'name: {self.name} Age: {self.age} Distict: {self.distic}')
#
# obj1 = myClass('alamin',21)
# obj1.name = "Tania"
# obj1.__class__.distic = 'Itali'
# obj1.display()
# obj2 = myClass('alamin',22)
# obj2.display()

# from string import ascii_letters
# # name = "almin 21 22 23"
# # keys = ''
# # value = []
# # for i in name:
# #     if i in ascii_letters:
# #         keys = keys+i
# #         #print(keys,end='')
# #     if i not in ascii_letters:
# #         value = list(i)
# #         #print(value,end='')
# # print(keys)
# # print(value)
# # print('---------------------')
# # lis = name.split(' ')
# # print(lis)
# # print(lis[1])
# # num = int(lis[1])
# # print(type(num))
# # print('--------------------------')
# # for a in lis:
# #     if type(a) == str:
# #         key = a
# #         print(key)
# #
# # m = '210'
# # n = int(m)
# # print(type(n))

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         line = input().split()
#         name, scores = line[0], line[1:]
#         scores = map(float, scores)
#         student_marks[name] = scores
#     query_name = input()
#     query_scores = student_marks[query_name]
#     print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))

