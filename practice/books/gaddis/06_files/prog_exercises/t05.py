from pathlib import Path

filepath = Path(__file__).parent / 'numbers.txt'

with open(filepath, 'w') as f:
    f.writelines([s + '\n' for s in '123456789'])

with open(filepath, 'r') as f:
    total = 0
    for line in f:
        total += int(line.strip('\n'))

    filepath.unlink()

    print(f'Sum of numbers from file "{filepath.name}": {total}')
