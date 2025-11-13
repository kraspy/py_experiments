from random import sample
from typing import Any

US_STATES = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'DC': 'District of Columbia',
}


def welcome_message(num_questions: int) -> None:
    print('*** Добро пожаловать на викторину: US States ***')
    print('Вам нужно ввести корректное название штата по сокращению.')
    print(f'Всего будет {num_questions} вопросов. Приступим!\n')


def check_questions_answers(
    questions: dict[str, Any],
) -> dict[str, tuple[bool, str, str]]:
    checked_questions = {}
    for q, a in questions.items():
        checked_questions[q] = (a.lower() == US_STATES[q].lower(), a, US_STATES[q])

    return checked_questions


def print_resuts(checked_answers: dict[str, tuple[bool, str, str]]) -> None:
    HEADER = '*** РЕЗУЛЬТАТЫ ***'
    for q, a in checked_answers.items():
        answer_is_correct, user_answer, correct_answer = a
        print('-' * len(HEADER))
        print(f'{q}\nВаш ответ: {user_answer}')
        print(f'{"✅ Верно!" if answer_is_correct else "❌ Ошибка"}')
        if not answer_is_correct:
            print(f'Правильный ответ: {correct_answer}')


def start_quiz(num_questions: int) -> None:
    welcome_message(num_questions)

    questions = dict.fromkeys(sample(list(US_STATES.keys()), k=5))

    for short_state in questions:
        questions[short_state] = input(f'Введите название штата "{short_state}": ')

    checked_answers = check_questions_answers(questions)

    print_resuts(checked_answers)


if __name__ == '__main__':
    start_quiz(5)
