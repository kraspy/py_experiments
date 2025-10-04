import turtle


def set_init_params(
    bg_color: str = '#000',
    color: str = '#f0f0f0',
    width: int = 800,
    height: int = 600,
):
    turtle.bgcolor(bg_color)
    turtle.color(color)
    turtle.setup(width, height)
