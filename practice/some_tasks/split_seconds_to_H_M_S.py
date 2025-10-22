def format_seconds(sec: int) -> tuple[int, ...]:
    """Выделение (часов, минут, секунд) из количества секунд

    Args:
        sec (int): Количество сенуд

    Raises:
        TypeError: sec (int) должно быть числом
        ValueError: sec (int) должно быть больше 0

    Returns:
        tuple(int, ...): (Часы, Минуты, Секунды)
    """
    if not isinstance(sec, int):
        raise TypeError('`sec` должно быть числом!')
    elif sec < 0:
        raise ValueError('Число должно быть больше 0!')

    hours = sec // 3600
    print(hours)
    minutes = (sec % 3600) // 60
    print(minutes)
    seconds = sec % 60
    print(seconds)

    return hours, minutes, seconds


def format_seconds2(sec: int) -> tuple[int, ...]:
    minutes, seconds = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)

    return hours, minutes, seconds
