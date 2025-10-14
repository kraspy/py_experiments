from _config import TMPFILE_PATH

with open(TMPFILE_PATH, 'r') as f:
    total = 0
    for line in f:
        total += int(line.strip('\n'))

    print(f'Sum of numbers from file "{TMPFILE_PATH.name}": {total}')
