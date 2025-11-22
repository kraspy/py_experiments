select * from family where description is null;

select * from family where description is null or family_name like '%Д%';

select family_id, family_name, coalesce(description, 'не заполнено') as description
from family;

