import re
from pathlib import Path

BASEDIR = Path(__file__).parent
FILEPATH = BASEDIR / 't05.txt'

with open(FILEPATH.resolve()) as f:
    text = f.read()
    words_list = list(set(map(str.lower, re.findall(r'\w+', text))))

print(', '.join(sorted(words_list)))
