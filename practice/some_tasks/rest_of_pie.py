def calc_rest(peoples: int, parts_of_pie: int) -> tuple[int, int]:
    """Вычислть сколько частей пирога достанестся каждому человеку и сколько частей пирога останется.

    Args:
        peoples (int): Количество людей
        parts_of_pie (int): Количество частей пирога

    Returns:
        tuple[int, int]: (ЧастейПирогаКаждому, Остаток)
    """
    return parts_of_pie // peoples, parts_of_pie % peoples


print(calc_rest(4, 25))
