from _utils import set_turtle_options
import turtle as t

set_turtle_options()

t.penup()
t.setx(-25)
t.sety(-55)
t.pendown()

for _ in range(8):
    t.forward(50)
    t.left(45)


t.penup()
t.home()
t.write('STOP', align='center')
t.hideturtle()

t.done()
