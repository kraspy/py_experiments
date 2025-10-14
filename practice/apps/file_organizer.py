import os
import random
from pathlib import Path

import click
from faker import Faker

BASE_DIR = Path(__file__).parent

DIRS_FILES_ASSOCIATIONS = {
    'images': ['jpg', 'jpeg', 'png', 'gif'],
    'videos': ['mp4', 'avi', 'mov'],
    'audios': ['mp3', 'wav', 'ogg'],
    'docs': ['txt', 'md'],
}

EXTENTIONS = [ext for exts in DIRS_FILES_ASSOCIATIONS.values() for ext in exts]

folders_association = {}

fkr = Faker()

fkr.file_path()


@click.group()
def cli():
    pass


@cli.command('organize')
@click.option('--input', default='unsorted_files')
@click.option('--output', default='sorted')
@click.option('--ignore', default='py')
def org(input, output, ignore):
    input_dir: Path = BASE_DIR / input
    output_dir: Path = BASE_DIR / output
    output_dir.mkdir(exist_ok=True)

    sorted_files_counter = 0

    unsorted_files_counter = 0

    for file in input_dir.iterdir():
        is_file_found = False
        for dir, ext in DIRS_FILES_ASSOCIATIONS.items():
            if file.suffix.lstrip('.') in ext:
                new_file_path = output_dir / dir / file.name
                if not new_file_path.parent.exists():
                    new_file_path.parent.mkdir()
                new_file_path = file.replace(output_dir / dir / file.name)
                sorted_files_counter += 1
                is_file_found = True
                print(
                    f'Файл "{file.name}" перемещен в "{new_file_path.relative_to(BASE_DIR)}"'
                )
                break

        if not is_file_found:
            unsorted_files_counter += 1

    print('=' * 40)
    print(f'Перемещено: {sorted_files_counter} файлов.')
    print(f'Не распознано: {unsorted_files_counter} файлов.')
    print('=' * 40)


@cli.command('generate')
@click.option('--output', type=click.STRING, default='unsorted_files')
@click.option('--number', type=click.INT, default=10)
def gen(
    number: int,
    output: str,
) -> bool:
    output_dir = BASE_DIR / output

    if not output_dir.exists():
        output_dir.mkdir()

    for file in range(number):
        ext = random.choice(EXTENTIONS)
        filename = fkr.file_name(extension=ext)

        with open(BASE_DIR / output / filename, 'wb') as f:
            filesize: int = random.randint(1, 5) * 1024
            f.write(os.urandom(filesize))


if __name__ == '__main__':
    cli()
