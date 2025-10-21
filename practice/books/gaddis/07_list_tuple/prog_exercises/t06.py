from math import pi


def show_numbers_more_than_pi(num_pi: float, numbers: list[int | float]):
    for number in numbers:
        if number > num_pi:
            print(number, end=', ')


show_numbers_more_than_pi(pi, [1, 2, 3, 4, 3.13, 3.14, 3.15])
