comment on table family is 'Семейство птиц';
comment on column family.family_id is 'Уникальный идентификатор семейства';
comment on column family.family_name is 'Название семейства';
comment on column family.description is 'Описание семейства';

comment on table genus is 'Род птиц';
comment on column genus.genus_id is 'Уникальный идентификатор рода';
comment on column genus.genus_name is 'Название рода';
comment on column genus.family_id is 'Ссылка на семейство';
comment on column genus.description is 'Описание рода';

comment on table species is 'Вид птиц';
comment on column species.species_id is 'Уникальный идентификатор вида';
comment on column species.species_name is 'Название вида';
comment on column species.description is 'Ссылка на род';
comment on column species.average_length is 'Описание вида';
comment on column species.average_weight is 'Средняя длина в см';
comment on column species.primary_color is 'Средний вес в г';
comment on column species.genus_id is 'Цвет оперения';

