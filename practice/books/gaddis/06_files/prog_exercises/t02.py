from io import TextIOWrapper
import click
import tempfile
import string
import random


def create_tmp_file() -> TextIOWrapper:
    fp = tempfile.TemporaryFile('tw+')
    return fp


def fill_text_file(file: TextIOWrapper, num_strings: int, line_len: int):
    for _ in range(num_strings):
        tmp_str = ''
        for _ in range(line_len):
            tmp_str += random.choice(string.ascii_letters)
        file.write(tmp_str + '\n')


@click.command()
@click.option('--head', type=click.INT, default=5)
def cli(head: int):
    f = None
    try:
        f = create_tmp_file()
        fill_text_file(f, 100, 30)

        f.seek(0)

        for _ in range(head):
            print(f.readline(), end='')

    except BaseException as e:
        print(e)
    finally:
        if f is not None:
            f.close()


if __name__ == '__main__':
    cli()
