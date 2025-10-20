from functools import reduce


num_list = input('Введите 20 числе с пробелом в качестве разделителя :').split(' ')

num_list = list(map(int, num_list))

print(f'наименьшее число в списке: {sorted(num_list)[0]}')
print(f'наибольшее число в списке: {sorted(num_list)[-1]}')
print(f'сумму чисел в списке: {reduce(lambda left, right: left + right, num_list, 0)}')
print(
    f'среднее арифметическое значение чисел в списке: {sum(num_list) / len(num_list)}'
)
