from _utils import input_number

MONTHS = 6

ccal_deficit: dict[str, float] = {
    'deficit': 500,
    'lost_kg': 1.5,
}

user_mass = input_number('Enter your mass (kg): ')

if user_mass <= 0:
    print('Your mass must be more than 0!')
    exit()

total_lost_weight = 0

for month in range(1, MONTHS + 1):
    total_lost_weight += ccal_deficit['lost_kg']
    print(f'Month #{month}: Total lost {total_lost_weight} kg')

print(
    f'🏁 For {MONTHS} months your weight will be: {user_mass - total_lost_weight:.2f}'
)
