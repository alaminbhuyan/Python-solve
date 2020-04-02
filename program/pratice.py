
# def fun1(n):
#     def fun2(m):
#         return m*n
#     return fun2
#
# obj1 = fun1(5)
# obj2 = fun1(5)
#
# print(obj1(2))
# print(obj2(3))
# print(obj1(obj2(4)))


def div(n1,n2):
    try:
        result = n1/n2
    except ZeroDivisionError:
        print('Oops zero not divide any number.please try again any valid number')
    else:
        print(result)
    finally:
        print('your work is done. Best of luck!!!')

a,b = map(int,input().split())
div(a,b)

