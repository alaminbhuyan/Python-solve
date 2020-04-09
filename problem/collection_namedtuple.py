from collections import namedtuple

# N = int(input())
# fields = input().split()
# total = 0
# for i in range(N):
#     students = namedtuple('Student',fields)
#     field1, field2, field3,field4 = input().split()
#     student = students(field1,field2,field3,field4)
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/N))


Car = namedtuple('car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print (xyz)
print (xyz.Class)

point = namedtuple('Point','x,y')
p1 = point(1,2)
p2 = point(3,4)
product = (p1.x*p2.x)+(p1.y*p2.y)
print(product)