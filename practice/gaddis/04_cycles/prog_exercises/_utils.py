from rich import print
import turtle as t


def input_number(prompt: str):
    try:
        number = int(input(prompt))
    except ValueError:
        print('[red]Invalid Number![/red]')
        exit()
    return number


def set_turtle_options(
    width: int = 500,
    height: int = 500,
    startx: int = 0,
    starty: int = 0,
    speed: int = 0,
):
    t.setup(
        width=width,
        height=height,
        startx=startx,
        starty=starty,
    )

    t.speed(speed)

    t.bgcolor('#000')
    t.color('#e0e0e0')
