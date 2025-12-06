from datetime import datetime, timedelta
from locale import LC_TIME, setlocale

setlocale(LC_TIME, 'ru_RU.UTF-8')

# 13.1
now = datetime.now().isoformat()
print(now)

# 13.2
today = datetime.fromisoformat(now)
print(today)

# 13.3
print(
    f'Год: {today.year}, Месяц: {today.month}, День: {today.day}\n'
    f'Время: {today.hour}:{today.minute}:{today.second}'
)

# 13.4
bd = datetime(1988, 6, 27)
print(bd)

# 13.5
print(bd.strftime('%A'))

# 13.6
print(bd + timedelta(days=10000))
