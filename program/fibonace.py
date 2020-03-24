"""num = int(input("Enter a number: "))
first,second = 0,1
print(first,end=" ")
print(second,end=" ")
for i in range(2,num+1):
    fibo = first + second
    first = second
    second = fibo
    print(fibo,end=" ")"""

n = input('Enter the number of terms: ')
def fibo(n):
    if n <= 1:
       return n
    else:
       return(fibo(n-1) + fibo(n-2))

for i in range(int(n)):
    print(fibo(i), end=' ')