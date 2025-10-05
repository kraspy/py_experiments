from rich import print


def convert_c_to_f(celsius: int) -> float:
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


for celsius in range(21):
    print(f'{celsius} C° = {convert_c_to_f(celsius):.2f} F°')
