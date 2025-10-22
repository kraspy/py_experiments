from decimal import Decimal
from math import ceil, floor
from textwrap import dedent

APP_NAME_DECO = '*'
APP_NAME = f'{APP_NAME_DECO} Расчет количества обоев {APP_NAME_DECO}'

APP_TEXT_LENGTH = len(APP_NAME)

WELCOME_TEXT = dedent(f"""
{'*' * APP_TEXT_LENGTH}
{APP_NAME}
{'*' * APP_TEXT_LENGTH}\n
""")


def main():
    print(WELCOME_TEXT)

    room_length = Decimal(input('Введите длину комнаты (м): '))
    room_width = Decimal(input('Введите ширину комнаты (м): '))
    room_height = Decimal(input('Введите высоту комнаты (м): '))

    room_windows_doors_area = Decimal(
        input('Введите суммарную площадь окон/дверей (м²): ')
    )

    roll_width = Decimal(input('Введите ширину рулона (м): '))
    roll_length = Decimal(input('Введите длину рулона (м): '))

    # Периметр комнаты = (ширина + длина) * 2
    # Площадь стен = ПериметрКомнаты * Высота
    walls_area = (
        2 * (room_length + room_width)
    ) * room_height - room_windows_doors_area

    # Площадь рулона
    roll_area = roll_width * roll_length

    # Площадь одной полосы обоев на стену
    one_strip_area = roll_width * room_height

    # Полос необходимо
    strips_needed = ceil(walls_area / one_strip_area)

    # Полос в руллоне
    strips_per_roll = floor(roll_length / room_height)

    rolls_needed = ceil(strips_needed / roll_area)

    print(
        dedent(f"""
            {'*' * APP_TEXT_LENGTH}
            {APP_NAME_DECO} S стен: {walls_area} м²
            {APP_NAME_DECO} S полосы обоев на стену: м²
            {APP_NAME_DECO} Нужно полос: {strips_needed} шт
            {APP_NAME_DECO} Полос в рулоне: {strips_per_roll} шт
            {APP_NAME_DECO} Кол-во рулонов: {rolls_needed} шт
            {'*' * APP_TEXT_LENGTH}
    """)
    )


if __name__ == '__main__':
    main()
