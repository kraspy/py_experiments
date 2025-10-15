from pathlib import Path

filepath = Path(__file__).parent / 'numbers.txt'

with open(filepath, 'w') as f:
    f.writelines([s + '\n' for s in '123456789a'])  # <- here is a wrong value

try:
    with open(filepath, 'r') as f:
        num_numbers = 0
        total = 0
        for line in f:
            total += int(line.strip('\n'))
            num_numbers += 1

        print(f'Average of numbers from file "{filepath.name}": {total / num_numbers}')
except IOError as e:
    print(e)
except ValueError as e:
    print(f'⛔ [ValueError]: {e}')
finally:
    filepath.unlink()
