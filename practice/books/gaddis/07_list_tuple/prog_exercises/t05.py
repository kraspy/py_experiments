with open('charge_accounts.txt', 'r', encoding='utf-8') as f:
    accounts = [num.strip() for num in f.readlines()]


while True:
    user_input = input('Введите номер счета или `exit` для выхода: ')
    if user_input == 'exit':
        break
    result = f'Номер счета "{user_input}" -'
    if user_input in accounts:
        print(result, 'допустимый номер.')
    else:
        print(result, 'НЕдопустимый номер.')
