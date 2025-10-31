def sum_multiples_3_5_less_than(num: int) -> int:
    """Возвращает сумму всех натуральных чисел меньше заданного значения, которые кратны 3 или 5.

    Args:
        num (int): Верхняя граница диапазона (не включительно)

    Returns:
        int: Сумма чисел
    """
    result = (num for num in range(1, num) if num % 3 == 0 or num % 5 == 0)

    return sum(result)


print(
    sum_multiples_3_5_less_than(1000),
)
