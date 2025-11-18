from pathlib import Path

BASEDIR = Path(__file__).parent.resolve()

START_YEAR = 1903

with open(BASEDIR / 'WorldSeriesWinners.txt') as f:
    years_teams_list = [team.strip() for team in f.readlines()]

    years_winners = {y: w for y, w in enumerate(years_teams_list, START_YEAR)}
    team_wins = {}

    for team in years_teams_list:
        team_wins[team] = team_wins.get(team, 0) + 1

user_input = int(input('Input year of The World Cup Games: '))

if not START_YEAR <= user_input <= list(years_winners.keys())[-1]:
    raise ValueError(f'Not found games in {user_input} year!')

winner = years_winners.get(user_input)
print(f'The Winner of {user_input} years: "{winner}"')
print(f'Team "{winner}" won {team_wins[winner]} times.')
