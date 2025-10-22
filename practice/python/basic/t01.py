user_input = input('Enter a number: ')

if user_input.isdigit():
    num = int(user_input)
    print(num * num)
    exit()

print('Wrong number!')
