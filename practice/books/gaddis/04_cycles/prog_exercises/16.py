import turtle as t
from _utils import set_turtle_options

set_turtle_options()

SQUARES = 100
SQUARE_SIZE = 2

t.penup()
t.goto(100, -100)
t.pendown()

t.seth(180)

squares = 0
for square in range(100):
    for _ in range(4):
        t.forward(square * SQUARE_SIZE)
        t.right(90)
    squares += 1

print(squares)
t.done()
