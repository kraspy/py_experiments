import json
from pathlib import Path

PARENT_DIR = Path(__file__).parent

json_string = '[]'

with open(PARENT_DIR / 'file.txt', 'w', encoding='utf-8') as f:
    py_obj: list = json.loads(json_string)

    py_obj.extend([i for i in range(10)])

    json.dump(py_obj, f, indent=2, separators=(',', ':'))


gen = [i + 1 for i in range(100)]

with open(PARENT_DIR / 'file_large.txt', 'w', encoding='utf-8') as f:
    for chunk in json.JSONEncoder(indent=2).iterencode(gen):
        f.write(chunk)
        f.flush()


json_obj = '{"a": 1, "b": 2, "c": ...}'

try:
    print(json.loads(json_obj))
except json.JSONDecodeError as e:
    print('Ошибка: ', e.msg)
    print('Строка/Колонка: ', e.lineno, '/', e.colno)
    print('Позиция: ', e.pos)
