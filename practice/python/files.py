from pathlib import Path
from faker import Faker

fkr = Faker(locale='ru_RU')

with open(
    './_tmpfile.txt',
    mode='w+',
    encoding='utf-8',
) as file:
    lines = (fkr.name() for _ in range(100))

    for line in lines:
        file.write(line + '\n')

    print(file.tell())
    print(file.seek(0))

    print(file.name)
    print(file.mode)
    print(file.closed)
    print(file.buffer)
    print(file.encoding)

    print(file.readline())

filepath = Path(file.name)
filepath.resolve().unlink()
