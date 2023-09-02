a = int(input("cheghadr daravordi? "))
s = 0
while a!=0:
    # s = s + 200
    s += a
    a = int(input("cheghadr daravordi? "))
print(f"Dar amade kol: s")

# turtle version
import turtle
a = int(turtle.textinput("?", "cheghadr daravordi? "))
s = 0
while a!=0:
    s += a
    a = int(turtle.textinput("?", "cheghadr daravordi? "))
turtle.write(f"Dar amade kol: {s}", font=('', 20))
turtle.done()