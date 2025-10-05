from _utils import input_number

user_input = input_number('Enter positive number (or negative for finish): ')

user_numbers: list[int] = []
while user_input > 0:
    user_numbers.append(user_input)
    user_input = input_number('Enter positive number (or negative for finish): ')

if len(user_numbers) == 0:
    user_numbers.append(0)
print(f'📥 Entered numbers: {user_numbers}')
print(f'🏁 Sum of your numbers: {sum(user_numbers)}')
