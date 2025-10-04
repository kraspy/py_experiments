from rich import print

try:
    user_num_input = int(input('Enter a positive number: '))
except ValueError:
    print('[red]Your value is not a number![/red]')
    exit(code=0)

if user_num_input >= 0:
    print(f'🏁 [green]OK: {user_num_input} is Positive number![/green] 🏁 ')
else:
    print('[red]Number must be more than 0![/red]')
