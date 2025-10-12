from _utils import set_turtle_options
import turtle as t

set_turtle_options()
t.penup()
t.setx(-100)
t.sety(200)
t.pendown()
t.seth(to_angle=270)

for _ in range(8):
    t.forward(200)
    t.left(135)

t.done()
