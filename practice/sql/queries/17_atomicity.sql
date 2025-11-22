---------------------
-- INSERT / SELECT --
---------------------
create table entity (
    entity_id bigint generated always as identity primary key,
    entity_name varchar(15) not null
);

insert into entity (entity_name) values
    ('entity0'),
    ('entity1'),
    ('entity2'),
    ('entity3');

create table entity_deleted (
    like entity
    including defaults
    including constraints
    including indexes
);

begin;
insert into entity_deleted
select * from entity
where entity_id in (1,2);
delete from entity where entity_id in (1,2);
commit; 

select * from entity;
select * from entity_deleted;

---------
-- CTE --
---------
with deleted_entities as (
    delete from entity
    where entity_id = 3
    returning *
)
insert into entity_deleted select * from deleted_entities;

