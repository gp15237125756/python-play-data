import math


def write():
    with open('text.txt', 'w') as f:
        f.write("hello,file")
        f.writelines("hello,file")
        f.close()


def read():
    with open('text.txt', 'r+') as f:
        c = f.readlines()
        print(c)
        f.seek(0)
        f.write("fuck you")
        f.seek(0)
        d = f.readlines()
        print(d)


def input():
    a=input('Enter your name')
    print(a)

input()
