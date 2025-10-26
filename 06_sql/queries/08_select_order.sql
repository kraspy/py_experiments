select * from family order by family_id desc;

table family order by family_id desc;

select * from family order by description nulls first;

select family_name from family where family_name like 'Д%' order by family_name;

select * from (
    values (2, 3), (3, 20), (2, 4), (1, 20), (3, 4), (1, 19)
) as something(a, b)
order by b desc, a asc;