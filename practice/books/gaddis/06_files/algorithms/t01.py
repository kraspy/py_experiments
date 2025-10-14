from faker import Faker
from _config import TMPFILE_PATH

fkr = Faker(locale='ru_RU')

with open(TMPFILE_PATH, 'w') as f:
    f.write(fkr.first_name())
