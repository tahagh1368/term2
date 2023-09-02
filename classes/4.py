# for i in range(10):
#     print('end')
import turtle
t = turtle.Pen()
for j in range(4):
    m = int(turtle.textinput("?", "Enter length: "))
    # m = int(input("Enter length: "))
    for i in range(4):
        t.fd(m)
        t.lt(90)
turtle.done()
