with open('WorldSeriesWinners.txt') as f:
    winners = [winner.strip().lower() for winner in f.readlines()]

user_team = input('Введите название команды: ').lower()

if user_team not in winners:
    print(f'Команды "{user_team}" нет в списке победителей.')
    exit()

num_of_years = winners.count(user_team)

print(f'Команда "{user_team}" побеждала {num_of_years} лет.')
