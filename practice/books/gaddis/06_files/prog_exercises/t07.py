from pathlib import Path
import random

filepath = Path(__file__).parent / 'numbers.txt'


def generate_radom_numbers(num: int = 5) -> list[int]:
    return [random.randint(1, 501) for _ in range(num)]


def main():
    NUMBER_OF_NUMBERS = 10

    with open(filepath, 'w') as f:
        str_of_nums = map(
            lambda num: str(num) + '\n',
            generate_radom_numbers(NUMBER_OF_NUMBERS),
        )
        f.writelines(str_of_nums)


if __name__ == '__main__':
    main()
    # filepath.unlink()
