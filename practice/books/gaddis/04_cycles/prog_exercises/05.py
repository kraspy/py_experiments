from _utils import input_number

years_number = input_number('Enter the number of years: ')

precipitations: list[int] = []
for year in range(1, years_number + 1):
    for month in range(1, 13):
        precipitation = input_number(
            'Enter the precipitation for year {year}, month {month}: '
        )

        precipitations.append(precipitation)

print(f'🌧️ Total: {sum(precipitations)} mm')
print(f'🌧️ Avg: {sum(precipitations) / len(precipitations)} mm')
