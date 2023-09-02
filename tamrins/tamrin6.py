import turtle
t = turtle.Pen()
colors = {
    'banafsh': 'purple',
    'purple': 'purple',
    'sabz': 'green',
    'green': 'green',
    'ghermez': 'red',
    'red': 'red',
    'ghermez': 'red',
    'abi': 'blue',
    'blue': 'blue',
    'zard': 'yellow',
    'yellow': 'yellow',
}
t.speed(0)
for i in range(1000000):
    c = turtle.textinput('Range Dayre', 'che rangi bashe?')
    t.color(colors.get(c, 'orange'))
    t.circle(100)
turtle.done()



