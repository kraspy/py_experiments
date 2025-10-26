select pg_column_size(1);
select pg_column_size(1::smallint);
select pg_column_size(1::int);
select pg_column_size(1::bigint);
select pg_column_size(1::real);
select pg_column_size(1::double precision);
select pg_column_size(1::numeric(5, 2));

select pg_column_size('a'::char);
select pg_column_size('a'::varchar);
select pg_column_size('a'::text);

select pg_column_size(true);

select pg_column_size(null);

select pg_column_size('2025-10-25'::date);

---
select pg_typeof(1);


-- NUMERIC round
select round(123.456::numeric, 2);

select length('wdq dsfsef12312312в3sef s'::text);