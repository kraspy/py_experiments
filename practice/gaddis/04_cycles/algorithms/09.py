from rich import print

try:
    user_num_input = int(input('Enter a number from 0 to 100: '))
except ValueError:
    print('[red]Your value is not a number![/red]')
    exit(code=0)

if 0 < user_num_input <= 100:
    print('🏁 [green]OK[/green] 🏁 ')
else:
    print('[red]Number must be from 0 to 100[/red]')
