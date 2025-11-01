from pathlib import Path


class TextFileWordCounter:
    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        self.lines = []
        self.average_words_in_sentence = 0

    def calculate_average_words_in_sentences(self):
        if not self.lines:
            with open(self.filepath) as f:
                while line := f.readline():
                    self.lines.append(line.strip().split(' '))

        words_in_lines = [len(line) for line in self.lines]

        print(words_in_lines)

        return sum(line for line in words_in_lines) / len(words_in_lines)


def main():
    twc = TextFileWordCounter(Path('.') / 't06_text.txt')

    result = twc.calculate_average_words_in_sentences()

    print(result)


if __name__ == '__main__':
    main()
