select * from family where family_name = 'Дроздовые';

select * from family where family_name in ('Дроздовые', 'Синицевые');

select * from family where family_name = 'Дроздовые' and family_name = 'Синицевые';

select * from family where family_name like '%а%';

select family_name from family where family_name ilike '%а%' or family_name ilike '%с%';

select * from family where family_name ~ 'а|с';

select * from family where regexp_count(family_name, 'а|с') > 0;