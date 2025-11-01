from pathlib import Path


class TextAnalyzer:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        self.indicators = {
            'upper_letters': 0,
            'lower_letters': 0,
            'digits': 0,
            'spaces': 0,
        }

    def calculate_indicators(self):
        with open(self.filepath) as f:
            text = f.read()

        if text:
            for letter in text:
                if letter.isupper():
                    self.indicators['upper_letters'] += 1
                if letter.islower():
                    self.indicators['lower_letters'] += 1
                if letter.isdigit():
                    self.indicators['digits'] += 1
                if letter.isspace():
                    self.indicators['spaces'] += 1

    def print_results(self):
        print('*' * 40)
        print(f'{self.indicators['upper_letters']=}')
        print(f'{self.indicators['lower_letters']=}')
        print(f'{self.indicators['digits']=}')
        print(f'{self.indicators['spaces']=}')
        print('*' * 40)
        print()


def main():
    ta = TextAnalyzer(Path('.') / 't06_text.txt')

    ta.calculate_indicators()

    ta.print_results()


if __name__ == '__main__':
    main()
