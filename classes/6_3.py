import turtle
t = turtle.Pen()
shape = ''
while shape!='exit':
    shape = turtle.textinput("command", "Enter command?")
    if shape.lower() == 'circle' or shape=='دایره':
        size = int(turtle.textinput("Radius", "enter radius?"))
        t.circle(size)
    elif shape=='rectangle':
        length = int(turtle.textinput("Lenght", "enter Length?"))
        height = int(turtle.textinput("Height", "enter Height?"))
        for i in range(2):
            t.fd(length)
            t.rt(90)
            t.fd(height)
            t.rt(90)
    elif shape == 'square':
        length = int(turtle.textinput("Lenght", "enter Length?"))
        for i in range(4):
            t.fd(length)
            t.rt(90)
    elif shape=='clear':
        t.clear()
    elif shape=='color':
        c = turtle.textinput("Color", "what color?")
        t.color(c)
# turtle.done()
