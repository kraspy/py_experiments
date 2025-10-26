select 'Птичка: ' || species_name as Птичка
from species
ORDER BY Птичка;

update species
set species_name = 'Древесный дрозд'
where species_name = 'Дрозд лесной';

update species
set species_name = 'Дрозд лесной'
where species_name = 'Древесный дрозд';

create table test.nums (a smallint);
insert into test.nums (a) values (1), (2), (3), (4), (5);
update test.nums set a = a ^ 2;
select * from test.nums;

drop table test.tmp_table;