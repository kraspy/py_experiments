drop role kraspy;

create role kraspy with login password '123';

create database db0
    with
    template=template0
    encoding='utf-8'
    lc_collate='ru_RU.UTF-8'
    lc_ctype='ru_RU.UTF-8'
    owner kraspy;