drop type if exists status;

create type status as enum (
    'черновик',
    'в работе'
);


select pg_column_size('черновик'::status);  -- 4
select pg_column_size('черновик');          -- 17
