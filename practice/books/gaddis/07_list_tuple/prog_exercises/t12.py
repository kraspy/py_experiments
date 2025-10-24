def check_simple_num(num: int) -> bool:
    is_simple = True
    for divider in range(2, num - 1):
        if num % divider == 0:
            is_simple = False
    return is_simple


user_number = int(input('Введите натуральное число: '))

numbers = (n for n in range(2, user_number + 1))

for n in numbers:
    is_simple = check_simple_num(n)
    print(f'Число "{n}" {"Простое" if is_simple else "Составное"}')
