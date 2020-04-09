# def Sort(sub_li):
#     sub_li.sort(key=lambda x: x[1])
#     return sub_li
# sub_li = [[1, 10], [2, 5], [3, 20], [4, 15]]
# print(Sort(sub_li))

sub_li = [[1, 10], [5, 5], [3, 20], [4, 15],[2,3]]

sub_li.sort(key=lambda  x:x[1])

print(sub_li)