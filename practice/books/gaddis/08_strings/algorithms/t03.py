my_string = 'a1b2c3'

digits_counter = 0
for i in range(len(my_string)):
    if my_string[i].isdigit():
        digits_counter += 1

print(f'В строке "{my_string}" {digits_counter} цифр(ы)')
