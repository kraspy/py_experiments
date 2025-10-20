import calendar

MONTHS = list(calendar.month_name)[1:]

year_rainfall = [
    int(input(f'Введите количество осадков за {MONTHS[i]}: '))
    for i in range(len(MONTHS))
]

report = """\
Суммарное количество осадков за год: {:.2f}
Среднее ежемесячное количество: {:.2f}
Месяц с наибольшим количеством осадков: {} ({:.2f})
Месяц с наименьшим количеством осадков: {} ({:.2f})
"""

print(
    report.format(
        sum(year_rainfall),
        sum(year_rainfall) / len(year_rainfall),
        MONTHS[year_rainfall.index(max(year_rainfall))],
        max(year_rainfall),
        MONTHS[year_rainfall.index(min(year_rainfall))],
        min(year_rainfall),
    )
)
