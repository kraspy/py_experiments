from functools import reduce

user_ints = input('Введите ряд чисел без разделителей: ')

if not user_ints.isdigit():
    raise ValueError('Можно вводить только числа!')

result = reduce(
    lambda x, y: int(x) + int(y),
    user_ints,
    0,
)

print(f'Сумма введенных вами чисел: {result}')
