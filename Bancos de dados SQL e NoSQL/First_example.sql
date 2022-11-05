show databases;
create database if not exists first_example;
use first_example;
create table person(
	person_id smallint unsigned,
    fname varchar(20),
    lname varchar(20),
    gender enum('F', 'M'),
    birth_date date,
    street varchar(30),
    city varchar(20),
    state varchar(20),
    country varchar(20),
    postal_code varchar(20),
    constraint pk_person primary key (person_id)
);

desc person;

create table favorite_food(
	person_id smallint unsigned,
    food varchar(20),
    constraint pk_favorite_food primary key (person_id, food),
    constraint fk_favorite_food_person_id foreign key (person_id) references person(person_id)
);

desc favorite_food;

#select * from information_schema.table_constraints where constraint_schema = 'first_example';

insert into person values('8','Vicente', 'Izel', 'M', '1992-10-29', 'Rua Cabral', 
							'Brasilia', 'BR', 'Brazil', '29554166');
                            
delete from person where person_id = 7 or person_id = 8;      

insert into favorite_food values(1, 'Pizza'), (2, 'Cachorro quente');               

select * from person;
select * from favorite_food;




