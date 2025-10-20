insert into family (family_name) values ('Синицевые');

insert into family (family_name, description) values
('Врановые', 'Семейство птиц, включающее воронов, грачей, сорок и других'),
('Дроздовые', 'Семейство певчих птиц, включающее дроздов, дрозд-рябинников и других');

insert into genus (genus_name, family_id) values
('Синица', 1),
('Гаичка', 1),
('Ворон', 2),
('Сорока', 2),
('Дрозд', 3);
