from datetime import date as d
from datetime import datetime as dt
from datetime import time as t
from datetime import timedelta as td
from datetime import timezone as tz
from datetime import tzinfo as tzi

# Create a date
datetime_obj = dt(2025, 11, 8, 16, 15, 14)

print(datetime_obj)


# Get current datetime
print(dt.today(), dt.now(), sep='\n')

print(dt.now(tz=tz.utc))


# Get date & time from datetime object

print(
    datetime_obj.date(),
    datetime_obj.time(),
    sep='\n',
)


# General attrs in datetime object
print(
    datetime_obj.year,
    datetime_obj.month,
    datetime_obj.day,
    datetime_obj.hour,
    datetime_obj.minute,
    datetime_obj.second,
    datetime_obj.microsecond,
    sep='\n',
)


# datetime from timestamp
ts = datetime_obj.timestamp()

print(ts, dt.fromtimestamp(ts), sep='\n')


# format output
print(datetime_obj.strftime('%d.%m.%Y %H:%M:%S'))


# Parse datetime from string
datetime_str = '08.11.2025 18:10:20+0700'
parsed_datetime = dt.strptime(datetime_str, '%d.%m.%Y %H:%M:%S%z')
print(f'{parsed_datetime!r}')


# ISO 8601
print(datetime_obj.isoformat())


# change parts of datetime
changed_datetime_obj = datetime_obj.replace(year=2000)
print(changed_datetime_obj)
print(datetime_obj)


# different between two datetimes
diff_timedelta = datetime_obj - changed_datetime_obj
print(
    type(diff_timedelta),
    diff_timedelta,
    diff_timedelta.days,
    diff_timedelta.seconds,
    diff_timedelta.total_seconds(),
    sep='\n',
)


# timedelta
td_30_days = td(
    days=7,
    hours=16,
    minutes=15,
    seconds=14,
)

print(
    datetime_obj,
    datetime_obj - td_30_days,
    sep='\n',
)


# compare two datetime objects
print(datetime_obj > changed_datetime_obj)
print(datetime_obj < changed_datetime_obj)


# day of week
print(
    dt.today().weekday(),
    dt.today().isoweekday(),
    sep='\n',
)


# isocalendar
print(
    datetime_obj.isocalendar(),
    dt.fromisoformat('2025-W45-6'),
    sep='\n',
)


# day of calendar (from 0001-01-01)
print(
    datetime_obj.toordinal(),
    dt.fromordinal(739563),
    sep='\n',
)


# combine date & time
new_dt = dt.combine(d(2025, 8, 11), t(22, 11, 10))
print(new_dt)


# convert naive datetime to other timezone
print(datetime_obj.astimezone(tz(td(hours=4))))


# ambiguoze times
print(datetime_obj.fold)


# UTC offset / DST
aware_datetime = dt.now(tz=tz.utc)
print(
    aware_datetime,
    aware_datetime.utcoffset(),
    aware_datetime.astimezone(tz(td(hours=7))).utcoffset(),
    aware_datetime.tzinfo,
    sep='\n',
)


# struct_time
print(datetime_obj.timetuple())
