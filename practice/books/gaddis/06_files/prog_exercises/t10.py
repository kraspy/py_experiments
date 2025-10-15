# 1 О. Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные.
# Президент клуба попросил вас написать две программы:
# • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры,
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь
# поле для имени игрока и поле для счета игрока);
# • программу, которая читает записи из файла golf.txt и выводит их на экран.
import click
from pathlib import Path

BASEDIR = Path(__file__).parent
filepath = BASEDIR / 'golf.txt'


def save(score: tuple[str, int]) -> str:
    with open(filepath, 'a') as f:
        s = f'Player: {score[0]}, Score: {str(score[1])}\n'
        f.write(s)
    return f'[SUCCESS] {s}'


@click.group()
def cli(): ...


@cli.command('set')
def set_score():
    player = input('Enter Player name: ')
    score = int(input(f'Enter "{player}\'s" score: '))

    save((player, score))


@cli.command('get')
def get_scores():
    with open(filepath) as f:
        print(f.read())


cli()
