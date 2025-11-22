select * from species
order by species_name, description
limit 10 offset 10;

select species_name, species_id
from species
where primary_color ilike '%белый%'
order by species_name
limit 5;