import random
from faker import Faker
from _config import TMPFILE_PATH

fkr = Faker(locale='ru_RU')

with open(TMPFILE_PATH, 'w') as f:
    for i in range(0, 20):
        if i == 14:
            f.write('Джон Перц, 50\n')
        else:
            f.write(f'{fkr.name()}, {random.randint(1, 100)}\n')

with open(TMPFILE_PATH, 'r') as f:
    new_file_path = TMPFILE_PATH.with_stem('tmp2')
    with open(new_file_path, 'w') as nf:
        for line in f:
            if 'Джон Перц' in line:
                continue
            else:
                new_line = line
            nf.write(new_line)
