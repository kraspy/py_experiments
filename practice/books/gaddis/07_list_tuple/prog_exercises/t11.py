magic_square = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6],
]


def check_magic_square(magic_square: list[list[list[int]]]) -> bool:
    is_magic_cube = True
    for line in range(3):
        if (
            not magic_square[line][0] + magic_square[line][1] + magic_square[line][2]
            == 15
        ):
            is_magic_cube = False
            break
    for column in range(3):
        if (
            not magic_square[0][column]
            + magic_square[1][column]
            + magic_square[2][column]
            == 15
        ):
            is_magic_cube = False
            break
    if not magic_square[0][0] + magic_square[1][1] + magic_square[2][2] == 15:
        is_magic_cube = False
    return True if is_magic_cube else False


res = check_magic_square(magic_square)
print(f'Квадрат {"Является" if res else "Не является"} магическим.')
