from faker import Faker
import pathlib

BASEDIR = pathlib.Path(__file__).parent

fkr = Faker()

filepath = BASEDIR / 'names.txt'

with open(filepath, 'w') as f:
    for _ in range(10):
        f.write(fkr.first_name() + '\n')


num_names = 0
with open(filepath) as f:
    for line in f:
        num_names += 1

filepath.unlink()

print(num_names)
