RESULT_TEXT = """\
*** РЕЗУЛЬТАТЫ ТЕСТА ***
*** {:^16} ***
************************
Количество правильных: {}
Количество неправильных: {}
Ответы: {}
"""

correct_answers = list('ACAADBCACBADCADCBBDA')

with open('t07_answers.txt') as f:
    student_answers = [a.strip() for a in f.readlines()]

test_results = [
    '+' if correct_answers[i] == student_answers[i] else '-'
    for i in range(len(correct_answers))
]

correct_answers_sum = test_results.count('+')
wrong_answers_sum = test_results.count('-')

res = RESULT_TEXT.format(
    'СДАЛ' if correct_answers_sum > 15 else 'НЕ СДАЛ',
    correct_answers_sum,
    wrong_answers_sum,
    test_results,
)

print(res)
