from _config import TMPFILE_PATH

with open(TMPFILE_PATH, 'w') as f:
    for i in range(1, 101):
        f.write(str(i) + '\n')
