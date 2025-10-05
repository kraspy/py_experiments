from _utils import input_number

init_population = input_number('Enter the initial population (int): ')
daily_growth = input_number('Enter the daily growth (%): ')
days = input_number('Enter the number of days (int): ')

total_population = init_population

print(f'Day #1     | {total_population:.3f}')
for day in range(2, days + 1):
    total_population += total_population * (daily_growth / 100)
    print(f'Day #{day:<5} | {total_population:.3f}')
