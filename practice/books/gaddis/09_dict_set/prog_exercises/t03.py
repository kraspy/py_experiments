from pathlib import Path

from _utils import char_codes as cc

BASE_DIR = Path(__file__)
FILENAME = Path('t03_source.txt')
FILEPATH = BASE_DIR.parent / FILENAME


def encode_text(text: str) -> str:
    return ''.join([cc[c] if c in cc else c for c in text])


def decode_text(text: str) -> str:
    codes_char = {code: char for char, code in cc.items()}
    return ''.join([codes_char[c] if c in codes_char else c for c in text])


def encode_file(filepath: Path) -> Path:
    with open(filepath.resolve(), 'rt', encoding='utf-8') as sf:
        file_text = sf.read()

    DEST_FILENAME = filepath.name.replace('source', 'encoded')
    DEST_FILE_PATH = filepath.parent / filepath.with_name(DEST_FILENAME)
    with open(DEST_FILE_PATH.resolve(), 'wt', encoding='utf-8') as ef:
        encoded_text = encode_text(file_text)
        ef.write(encoded_text)

    return DEST_FILE_PATH


def decode_file(filepath: Path) -> str:
    with open(filepath.resolve(), 'rt', encoding='utf-8') as f:
        file_text = f.read()
        print(file_text)

    return decode_text(file_text)


def main():
    new_file_path = encode_file(FILEPATH)

    print(decode_file(new_file_path))


if __name__ == '__main__':
    main()
