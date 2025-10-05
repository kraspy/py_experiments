from _utils import input_number

user_num = input_number('Enter positive number: ')

if user_num <= 0:
    print('❌ Number must be more than 0!')
    exit()

factorial = 1
for i in range(1, user_num + 1):
    factorial *= i

print(f'🏁 Factorial of {user_num} is: {factorial}')
