from rich import print

# 1
while True:
    try:
        num = int(input('Enter a number:'))
    except ValueError:
        print('[red]Invalid Number![/red]')
        break

    product = num * 10
    print(f'{product=}')
    if product >= 100:
        print('🏁 [green]Finish[/green] 🏁 ')
        break
