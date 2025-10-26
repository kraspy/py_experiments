select 'ab'::char;

select pg_typeof('abc');

select length('abc');

select 'abc' || 'def';

select format('this is %s%s', 'sparta', '!');

select replace('hello', 'o', '');

select position('o' in 'hello');

select substring('Hello, World!' from 8 for 1000);

select upper('Hello');
select lower('WoRlD');

select split_part('2025-10-25', '-', 1);

select to_date('26.10.2025', 'DD.MM.YYYY');

select to_timestamp('26.10.2025', 'DD.MM.YYYY');