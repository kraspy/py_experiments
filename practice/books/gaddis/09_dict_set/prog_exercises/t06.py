from pathlib import Path

from rich import print

BASE_DIR = Path(__file__).resolve().parent

ALL_TEXT = '[green]All words[/green]: '
UNIQUE_ALL_TEXT = '[green]Unique from both files[/green]: '
UNIQUE_FIRST_TEXT = '[green]Unique from first file[/green]: '
UNIQUE_SECOND_TEXT = '[green]Unique from second file[/green]: '
UNIQUE_NOT_ALL = '[green]Unique not in both files[/green]: '


with open(BASE_DIR / 't06.txt') as f:
    words_1 = f.readline().strip().split(' ')
    words_2 = f.readline().strip().split(' ')


set_words_1 = set(words_1)
set_words_2 = set(words_2)

print(
    f'{UNIQUE_ALL_TEXT}{", ".join(set_words_1.union(set_words_2))}',
)
print(
    f'{ALL_TEXT}{", ".join([*words_1, *words_2])}',
)
print(
    f'{UNIQUE_FIRST_TEXT}{", ".join(set_words_1.difference(set_words_2))}',
)
print(
    f'{UNIQUE_SECOND_TEXT}{", ".join(set_words_2.difference(set_words_1))}',
)
print(
    f'{UNIQUE_NOT_ALL}{", ".join(set_words_1.symmetric_difference(set_words_2))}',
)
