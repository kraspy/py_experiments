MONTHS = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]


def get_user_input_date(text: str) -> str:
    return input(text)


def format_date(date: str) -> str:
    day, month, year = date.split('/')

    return f'{day} {MONTHS[int(month.lstrip("0"))]} {year} г.'


def main():
    user_date = get_user_input_date('Введите дату в формате "дд.мм.гггг": ')

    print(format_date(user_date))


if __name__ == '__main__':
    main()
