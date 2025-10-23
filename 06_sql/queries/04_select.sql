select * from genus; -- table genus;

select genus_name from genus;

select genus_name, genus_id from genus;

select genus_name as bird_genus, genus_id from genus;

select genus_name as bird_genus, genus_id from postgres.public.genus;