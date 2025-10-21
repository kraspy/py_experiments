boys_names_file = 'BoyNames.txt'
girls_names_file = 'GirlNames.txt'

with open(boys_names_file) as f:
    boys_names = [name.strip() for name in f.readlines()]

with open(girls_names_file) as f:
    girls_names = [name.strip() for name in f.readlines()]

print('*' * 20)
print("""\
Введите число пункта меню и нажмите Enter:
1 - Проверить имя мальчика
2 - Проверить имя девочки
3 - Проверить имя мальчика и девочки""")
user_input = input('Ваш выбор: ')

boy_name = None
girl_name = None

if user_input == '1':
    boy_name = input('Введите имя мальчика: ')
elif user_input == '2':
    girl_name = input('Введите имя девочки: ')
elif user_input == '3':
    boy_name = input('Введите имя мальчика: ')
    girl_name = input('Введите имя девочки: ')
else:
    print('Некорректный выбор')

if boy_name:
    bn = boy_name
    print(
        f'{bn} - популярное имя'
        if boy_name in boys_names
        else f'{bn} - не популярное имя'
    )
if girl_name:
    gn = girl_name
    print(
        f'{gn} - популярное имя'
        if girl_name in girls_names
        else f'{gn} - не популярное имя'
    )
