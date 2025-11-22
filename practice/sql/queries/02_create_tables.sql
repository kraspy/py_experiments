create table family (
    family_id bigint generated always as identity primary key,
    family_name varchar(150) not null,
    description text
);

create table genus (
    genus_id bigint generated always as identity primary key,
    genus_name varchar(150) not null,
    description text,
    family_id bigint not null references family(family_id)
);

create table species (
    species_id bigint generated always as identity primary key,
    species_name varchar(150) not null,
    description text,
    average_length smallint not null check (average_length > 0),
    average_weight smallint not null check (average_weight > 0),
    primary_color varchar(50) not null,
    genus_id bigint not null references genus(genus_id)
);

create schema test;

create table test.tmp_table as (
    select species_id, species_name from species 
    where species_name ilike 'синица%'
);

select species_name into test.tmp_table
from species
where species_name ilike 'Синица%';
