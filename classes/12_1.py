from turtle import *
def square(a=100, c='black', jahat='left', x=0, y=0, color2='black'):
    up()
    goto(x, y)
    down()
    fillcolor(color2)
    pencolor(c)
    begin_fill()
    for i in range(4):
        fd(a)
        if jahat=='left':
            lt(90)
        elif jahat=='right':
            rt(90)
    end_fill()
square(200, 'green', 'left', 0, 0, '#ff0100')
square(150, 'red', 'left', 50, 50, 'blue')
square(100, 'blue', 'right', -200, -50, 'red')
square(x=-150)
square()

done()