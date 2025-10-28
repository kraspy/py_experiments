my_string = 'aAbBcC'

islower_counter = 0
for i in range(len(my_string)):
    if my_string[i].islower():
        islower_counter += 1

print(f'В строке "{my_string}" {islower_counter} символ(ов) в нижнем регистре')
