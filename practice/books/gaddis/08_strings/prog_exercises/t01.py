BIG_RUSSIAN_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
SMALL_RUSSIAN_LETTERS = BIG_RUSSIAN_LETTERS.lower()

ALLOW_SYMBOLS = BIG_RUSSIAN_LETTERS + SMALL_RUSSIAN_LETTERS + '-'


def short_fullname(fullname: str) -> str:
    if len(splitted_name := fullname.split(' ')) < 3:
        raise ValueError('ФИО должно состоять из 3 слов!')

    for part_of_name in splitted_name:
        for letter in part_of_name:
            if letter not in ALLOW_SYMBOLS:
                print(f'"{letter}" - недопустимый символ!')
                raise ValueError('Части ФИО должны состоять только из букв и дефисов!')

    last_name, first_name, patronymic = splitted_name

    return (
        f'{last_name.capitalize()} {first_name.upper()[:1]}. {patronymic.upper()[:1]}.'
    )


shorted_name = short_fullname('Петров Иван Иванович')

print(shorted_name)
