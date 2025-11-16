import re
from pathlib import Path

BASEDIR = Path(__file__).parent
FILEPATH = BASEDIR / 't05.txt'

counter = {}

with open(FILEPATH.resolve()) as f:
    text = f.read()
    words_list = list(map(str.lower, re.findall(r'\w+', text)))

for word in words_list:
    counter[word.lower()] = counter.get(word, 0) + 1


asc_sorted_counter = dict(
    sorted(counter.items(), key=lambda x: (x[1], x[0]), reverse=True)
)

for word, count in asc_sorted_counter.items():
    print(f'Слово "{word}" встречается в тексте {count} раз.')
