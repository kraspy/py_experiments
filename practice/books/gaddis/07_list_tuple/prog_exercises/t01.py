import calendar

INIT_MESSAGE = """\
Давайте посчитаем продажи магазина за неделю! 💰

Для этого вам нужно ввести сумму продаж за каждый день.
"""
DAYS = calendar.day_name

print(INIT_MESSAGE)
sales = [int(input(f'Сумма продаж за {DAYS[i]}: ')) for i in range(len(DAYS))]

print(f'Сумма продаж за неделю: {sum(sales)} ед.')
