from rich import print

ccal_per_min = 4.2

distances = [10, 15, 20, 25, 30]

for distance in distances:
    burned_ccal = distance * ccal_per_min
    print(f'[red]{burned_ccal}[/red] ccal for {distance} min')
