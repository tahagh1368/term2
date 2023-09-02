import turtle
t = turtle.Pen()
t.speed(0)
for i in range(1000000):
    c = turtle.textinput('Range Dayre', 'che rangi bashe?')
    if c=='sabz' or c=='سبز' or c=='green':
    # if c in ('sabz', 'سبز', 'green'):
        c='green'
    elif c=='ghermez' or c=='قرمز':
        c='red'
    elif c=='abi':
        c='blue'
    elif c=='zard':
        c='yellow'
    t.color(c)
    t.circle(100)
turtle.done()

