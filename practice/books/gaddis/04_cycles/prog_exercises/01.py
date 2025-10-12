collect_days = 5
total_errors = 0

for day in range(1, collect_days + 1):
    try:
        today_errors = int(input('How many errors did you make today? '))
    except ValueError:
        print('[red]Invalid Number![/red]')
        break

    total_errors += today_errors
    print(f'Day {day}: {today_errors} errors')

print(f'🧮 Total errors: {total_errors}')
