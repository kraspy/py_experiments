from _config import TMPFILE_PATH

with open(TMPFILE_PATH) as f:
    print(f.tell())
    print(f.read())
    print(f.tell())
