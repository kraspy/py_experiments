create table entity (
    entity_id bigint generated always as identity primary key,
    entity_name varchar(20) not null unique,
    is_deleted boolean not null default False
);

insert into entity (entity_name) values
    ('entity0'),
    ('entity1'),
    ('entity2'),
    ('entity3');

update entity set is_deleted = True
where entity_id in (1,2);

select * from entity where is_deleted;