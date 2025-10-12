if True:
    print('True')
elif False:
    print('False')
else:
    print('Never')


a = 'ternary' if True else 'operator'

tuple_coords = (0, 1)
match tuple_coords:
    case (0, 0):
        print('0, 0')
    case (0, y):
        print(f'0, {y}')
    case _:
        print('default value')


print(('False', 'True')[True])  # bool - подкласс int
print(bool.__mro__)

answers = {
    'q1': 'answer 1',
    'q2': 'answer 2',
    'q3': 'answer 3',
}

print(answers.get('q5', 'Unknown'))
