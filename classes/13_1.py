def add2(a=0, b=0):
    return a+b

def add3(a, b, c):
    return a+b+c

def add4(a, b, c, d):
    return a+b+c,d

from tkinter import *
def add(a, b, *args, **kwargs):
    print(args)
    print(kwargs)
    return a+b
print(add(4, 7, 6, 8,9,8, color='red', background_color='blue', mohammad='salam'))
