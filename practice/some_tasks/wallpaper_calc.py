from decimal import Decimal

import typer


def main():
    room_width = Decimal(input('Введите ширину комнаты (м): '))
    room_length = Decimal(input('Введите длину комнаты (м): '))
    room_height = Decimal(input('Введите высоту комнаты (м): '))

    roll_width = Decimal(input('Введите ширину рулона (м): '))
    roll_length = Decimal(input('Введите длину рулона (м): '))

    walls_area = ((room_width * room_length) * 2) * room_height
    roll_area = roll_width * roll_length

    rolls_neded = walls_area / roll_area

    info = f"""\
    Площадь стен: {walls_area} м²
    Площадь рулона: {roll_area} м²

    Необходимо рулонов: {rolls_neded} шт.
    """

    print(info)


if __name__ == '__main__':
    typer.run(main)
