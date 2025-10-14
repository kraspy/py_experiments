from _config import TMPFILE_PATH

with open(TMPFILE_PATH, 'r') as f:
    for line in f:
        print(line.rstrip('\n'), end=' | ')
