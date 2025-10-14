import random
from faker import Faker
from _config import TMPFILE_PATH

fkr = Faker(locale='ru_RU')

with open(TMPFILE_PATH, 'w') as f:
    for i in range(0, 20):
        if i == 14:
            f.write('Джулия Милан, 50\n')
        else:
            f.write(f'{fkr.name()}, {random.randint(1, 100)}\n')

with open(TMPFILE_PATH, 'r') as f:
    new_file_path = TMPFILE_PATH.with_stem('tmp2')
    with open(new_file_path, 'w') as nf:
        for line in f:
            if 'Джулия Милан' in line:
                splitted_line = line.split(', ')
                new_line = f'{splitted_line[0]}, 100\n'
            else:
                new_line = line
            nf.write(new_line)
