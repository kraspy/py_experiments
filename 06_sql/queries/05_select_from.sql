-- for example
create view view_name as
select family_id, family_name from family;



-- Queries
select 1 + 1 as num;

select * from family;

select * from (
    select family_name from family
);

select * from postgres.public.view_name;

select num from generate_series(1, 10) as num;

select * from (
    values
        (1, 'User1'),
        (2, 'User2')
) as t(id, name);

select genus_name from (
    select * from genus
);

select generate_series(
    '2020-01-01'::date,
    '2024-06-01'::date,
    '2 months'::interval) date;

select date from generate_series(
    '2020-01-01'::date,
    '2024-06-01'::date,
    '2 months'::interval) date;
                       
select date from generate_series(
    date '2020-01-01',
    date '2024-06-01',
    interval '2 month'
) as date;

select * from (
	values (
		(The Shawshank Redemption, 9.3, 1994),
		(The Godfather, 9.2, 1972),
		(The Dark Knight, 9.1, 2008),
		(Inception, 8.8, 2010)
	) as t(movie, imdb_rating, year)
);