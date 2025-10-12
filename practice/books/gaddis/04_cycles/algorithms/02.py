from rich import print

# 2
flag = 'y'
while flag == 'y':
    try:
        number_1 = int(input('Enter a number: '))
        number_2 = int(input('Enter another number: '))

    except ValueError as e:
        print('[red]Invalid Number![/red]')
        print(e)
        continue

    print(f'{number_1} + {number_2} = {number_1 + number_2}')

    flag = input('Do you want to continue? (y/n): ')
    while (flag != 'y') and (flag != 'n'):
        print('[red]Invalid Answer![/red]')
        flag = input('Do you want to continue? (y/n): ')
        continue
    if flag == 'y':
        print('[green]Next question...[/green]')
        continue
    elif flag == 'n':
        print('🏁 [green]Finish[/green] 🏁 ')
        break
