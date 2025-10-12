from _utils import input_number

days = input_number('Enter the number of days: ')

total = 0

for day in range(days):
    total += 1
    print(f'Day #{day + 1:<5} | {total} pennies.')

print(f'💰 Total: {total / 100:.2f} rub.')
