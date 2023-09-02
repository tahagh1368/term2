import turtle
t = turtle.Pen()
shape = turtle.textinput("shape", "what shape?")
if shape == 'circle':
    size = int(turtle.textinput("Radius", "enter radius?"))
    t.circle(size)
elif shape=='rectangle':
    pass
elif shape == 'square':
    pass
turtle.done()