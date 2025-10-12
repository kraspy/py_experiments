from rich import print


def calc_distance(speed: int, hours: int) -> float:
    distance = speed * hours
    return distance


try:
    user_input_speed = int(input('Enter speed (km/h): '))
    user_input_hours = int(input('Enter hours: '))
except ValueError:
    print('[red]Invalid Number![/red]')
    exit()

distance = calc_distance(user_input_speed, user_input_hours)

print(f'{"Час":<10}|{"Расстояние":<10}')
print('*' * 21)

for hour in range(1, user_input_hours + 1):
    print(f'{hour:<10}|{calc_distance(user_input_speed, hour):<10}')
