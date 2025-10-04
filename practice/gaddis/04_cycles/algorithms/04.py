from rich import print
from array import array


def show_numbers(array_of_nums: array[int]):
    return '+'.join(map(str, array_of_nums))


array_of_ints = array('i')
result = 0

for i in range(10):
    try:
        current_value = int(input('Enter a number: '))
    except ValueError:
        print('[red]Invalid Number![/red]')
        continue

    array_of_ints.append(current_value)
    result += current_value
    print(show_numbers(array_of_ints), '=', result)

print('🏁 [green]Finish[/green] 🏁 ')
print(show_numbers(array_of_ints), '=', result)
