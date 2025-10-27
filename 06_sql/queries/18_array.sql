drop table if exists arr;

create table arr (
    arr_int int[],
    arr_text text[],
    arr_date date[]
);

insert into arr values (
    '{1,2,3,4,5}',
    '{"1", "2", "3", "4", "5"}',
    '{"2025-10-26", "2025-10-27", "2025-10-28"}'
);

select * from arr;

update arr set arr_int = array_append(arr_int, 10);

select * from arr;

select 1=any('{1,2,3}'::int[]);

select arr_int from arr
where 1=any(arr_int);

select arr_int[1], arr_int[2] from arr;

select unnest(arr_int) from arr;

select unnest(string_to_array('1, 2, 3', ', '));

select array_to_string('{"a", "b", "c"}'::text[], '-');

select * from unnest('{1, 2}'::int[], '{3,4}'::int[]);
