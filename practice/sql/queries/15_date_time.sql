-- DATE
select '2025-10-26'::date;

-- TIME
select '10:00:00'::time; 

-- TIMETZ
select '10:00:00 +0700'::timetz at time zone 'Europe/Moscow';

-- TIMESTAMP
select pg_typeof('2025-10-26 10:00'::timestamp);
select '2025-10-26 10:00'::timestamp;

-- TIMESTAMPTZ
select pg_typeof(current_timestamp);
select pg_typeof(now());

select now();

-- INTERVAL
select '1 hour'::interval;

select pg_typeof(now() - '1 hour'::interval);

select 
    now()                      as current_time,
    now() - '1 year'::interval as one_year_ago;

select '2025-10-26'::date - '2020-10-26'::date;

select now() - (now() - '5 year'::interval);

-------------------------
-- DATE/TIME FUNCTIONS --
-------------------------
select age('2025-10-26 10:00:00'::timestamp, '2020-06-23 07:59:00'::timestamp);

select extract(year from '2025-10-26'::date);   -- 2025
select extract(month from '2025-10-26'::date);  -- 10
select extract(day from '2025-10-26'::date);    -- 26

select to_char(now() at time zone 'Asia/Krasnoyarsk', 'DD.MM.YYYY HH24:MI:SS');

select date_trunc('month', now());

--------------
-- PRACTICE --
--------------
select 
    to_char(created_at, 'DD.MM.YYYY HH24:MI:SS') as "дата иинцедента",
    message as сообщение
from log;

insert into log (created_at, message)
values
    ('2024-07-31 20:19:51'::timestamp, 'Произошло страшное: сломался приём платежа #1128'),
    ('2024-07-31 17:19:52'::timestamp, 'Трындец с отправкой почты, похоже, почтовый сервер недоступен!'),
    ('2024-07-31 17:20:53'::timestamp, 'Ужас, всё работает!');

select * from logs
where date_trunc('month', created_at) = date_trunc('month', now);

select * from log
where created_at >= current_date - '7 day'::interval and created_at <= now()
order by created_at;

select current_date - '30 day'::interval;

delete from log
where created_at < current_date - '30 day'::interval;

select '2025-01-31 10:20:30'::timestamp + '1 month'::interval;

select pg_typeof('2025-10-25'::date - '2025-10-01'::date);
select pg_typeof('2025-10-25'::timestamp - '2025-10-01'::date);

select 
    to_char(start, 'DD.MM.YYYY')  as start,
    to_char(finish, 'DD.MM.YYYY') as finish,
    (finish::date - start::date)  as delta_in_days
from records
order by start, finish;

select
    to_char(start, 'DD.MM.YYYY')  as start,
    to_char(finish, 'DD.MM.YYYY') as finish,
    age(finish, start) as delta
from records
order by start, finish;

select email
from embloyees
where extract(month from birthday) = 4
order by email;
