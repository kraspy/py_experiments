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