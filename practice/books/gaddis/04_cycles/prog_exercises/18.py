from _utils import set_turtle_options
import turtle as t

set_turtle_options()

SIDE_SIZE = 2

t.left(90)

current_side_size = SIDE_SIZE
for _ in range(20):
    for _ in range(4):
        current_side_size += SIDE_SIZE
        t.forward(current_side_size)
        t.left(90)

t.hideturtle()

t.done()
