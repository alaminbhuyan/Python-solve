import math

a = float(input("Insert coefficient a: "))
b = float(input("Insert coefficient b: "))
c = float(input("Insert coefficient c: "))

discriminant = b**2 - 4 * a * c

if discriminant >= 0:
    x_1=(-b+math.sqrt(discriminant))/2*a
    x_2=(-b-math.sqrt(discriminant))/2*a
else:
    x_1= complex((-b/(2*a)),math.sqrt(-discriminant)/(2*a))
    x_2= complex((-b/(2*a)),-math.sqrt(-discriminant)/(2*a))

if discriminant > 0:
    print("The function has two distinct real roots: {} and {}".format(x_1,x_2))
elif discriminant == 0:
    print("The function has one double root: ", x_1)
else:
    print("The function has two complex (conjugate) roots: {}  and {}".format(x_1,x_2))