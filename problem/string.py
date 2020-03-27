
# txt = "hi i am alamin"
# txt2 = txt.split(' ')
# print(txt2)
# txt3 = "-".join(txt2)
# print(txt3)

def print_full_name(a, b):
    full_name = a+b
    if len(full_name)<=20:
        print("Hello {a} {b}! You just delved into python.".format(a=a, b=b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)