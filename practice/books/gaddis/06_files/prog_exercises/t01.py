import tempfile
import random

fd, fp = tempfile.mkstemp('.txt', 'tmp_', text=True)

with open(fp, 'w') as f:
    f.writelines([f'{random.randint(1, 20)}\n' for _ in range(20)])

with open(fp) as f:
    for value in f:
        print(value, end='')
