from pathlib import Path

filepath = Path(__file__).parent / 'numbers.txt'

with open(filepath, 'r') as f:
    num_numbers = 0
    total = 0
    for line in f:
        total += int(line.strip('\n'))
        num_numbers += 1

    filepath.unlink()

    print(f'Sum: {total}\nNum: {num_numbers}')
