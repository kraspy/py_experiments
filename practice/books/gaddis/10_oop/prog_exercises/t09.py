class Question:
    def __init__(
        self, question_text, answer1, answer2, answer3, answer4, correct_answer_num
    ):
        self._question_text = question_text
        self._answer1 = answer1
        self._answer2 = answer2
        self._answer3 = answer3
        self._answer4 = answer4
        self._correct_answer_num = correct_answer_num

    def get_question_text(self):
        return self._question_text

    def get_answer1(self):
        return self._answer1

    def get_answer2(self):
        return self._answer2

    def get_answer3(self):
        return self._answer3

    def get_answer4(self):
        return self._answer4

    def get_correct_answer_num(self):
        return self._correct_answer_num

    def set_question_text(self, text):
        self._question_text = text

    def set_answer1(self, answer):
        self._answer1 = answer

    def set_answer2(self, answer):
        self._answer2 = answer

    def set_answer3(self, answer):
        self._answer3 = answer

    def set_answer4(self, answer):
        self._answer4 = answer

    def set_correct_answer_num(self, num):
        if 1 <= num <= 4:
            self._correct_answer_num = num
        else:
            raise ValueError('Номер правильного ответа должен быть от 1 до 4.')


questions = [
    Question(
        'Функция для приведения строки к нижнему регистру называется',
        'lower',
        'upper',
        'capitalize',
        'title',
        1,
    ),
    Question(
        'Функция для приведения строки к верхнему регистру называется',
        'lower',
        'upper',
        'capitalize',
        'title',
        2,
    ),
    Question(
        'Функция для приведения первой буквы строки к верхнему регистру называется',
        'lower',
        'upper',
        'capitalize',
        'title',
        3,
    ),
    Question(
        'Функция для приведения всех первых каждого слова в строке к верхнему регистру называется',
        'lower',
        'upper',
        'capitalize',
        'title',
        4,
    ),
    Question(
        'Модуль для работы с СУБД SQLite называется',
        'sqlite',
        'sqlite3',
        'sqlite4',
        'sqlite5',
        2,
    ),
    Question(
        'Ключевое слово для создания класса',
        'class',
        'def',
        'func',
        'method',
        1,
    ),
    Question(
        'Ключевое слово для создания функции',
        'class',
        'def',
        'func',
        'method',
        2,
    ),
    Question(
        'Является ли список (list) изменяемым типом данных?',
        'Да',
        'Нет',
        'Иногда',
        'Зависит от содержимого',
        1,
    ),
    Question(
        'Является ли кортеж (tuple) изменяемым типом данных?',
        'Да',
        'Нет',
        'Иногда',
        'Зависит от содержимого',
        2,
    ),
    Question(
        'Каким типом данных должен быть ключ словаря (dict)?',
        'Изменяемым',
        'Неизменяемым',
        'Только строкой',
        'Только числом',
        2,
    ),
]


def play_game():
    p1_score = 0
    p2_score = 0

    print('Добро пожаловать в Викторину!')
    print('Игроки отвечают по очереди.')

    for i, q in enumerate(questions):
        player = 1 if i % 2 == 0 else 2
        print(f'\nВопрос {i + 1} (Игрок {player}):')
        print(q.get_question_text())
        print(f'1. {q.get_answer1()}')
        print(f'2. {q.get_answer2()}')
        print(f'3. {q.get_answer3()}')
        print(f'4. {q.get_answer4()}')

        while True:
            try:
                choice = int(input('Ваш ответ (1-4): '))
                if 1 <= choice <= 4:
                    break
                print('Пожалуйста, введите число от 1 до 4.')
            except ValueError:
                print('Пожалуйста, введите число.')

        if choice == q.get_correct_answer_num():
            print('Правильно!')
            if player == 1:
                p1_score += 1
            else:
                p2_score += 1
        else:
            print('Неправильно.')

    print('\n' + '=' * 20)
    print('Результаты:')
    print(f'Игрок 1: {p1_score}')
    print(f'Игрок 2: {p2_score}')
    print('=' * 20)

    if p1_score > p2_score:
        print('Победил Игрок 1!')
    elif p2_score > p1_score:
        print('Победил Игрок 2!')
    else:
        print('Ничья!')


if __name__ == '__main__':
    play_game()
