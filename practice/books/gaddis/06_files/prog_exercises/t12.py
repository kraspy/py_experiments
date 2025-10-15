# steps.txt. Этот файл содержит количество
# шагов, которые человек делал каждый день в течение года. В файле 365 строк, и каждая
# строка содержит количество шагов, сделанных в течение дня. (Первая строка - это число
# шагов, сделанных 1 января, вторая строка- число шагов, сделанных 2 января, и т. д.)
# Напишите программу, которая читает файл и затем выводит среднее количество шагов,
# сделанных в течение каждого месяца. (Данные были записаны в год, который не был
# високосным, и поэтому февраль имеет 28 дней.)
import calendar

months = [
    'JAN',
    'FEB',
    'MAR',
    'APR',
    'MAY',
    'JUN',
    'JUL',
    'AUG',
    'SEP',
    'OCT',
    'NOV',
    'DEC',
]

avg_steps = dict().fromkeys(
    months,
    0.0,
)

with open('steps.txt') as f:
    for month_idx in range(len(months)):
        steps_in_month = 0
        days_in_month = calendar.monthrange(2025, month_idx + 1)[1]

        for _ in range(days_in_month):
            line = f.readline()
            steps_in_month += int(line)

        avg_steps[months[month_idx]] = steps_in_month / days_in_month

for k, v in avg_steps.items():
    print(f'{k}: {v:.2f} steps')
