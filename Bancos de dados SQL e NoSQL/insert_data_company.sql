show databases;

use company;
show tables;

select * from employee;

insert into employee values('Marcus', 'V', 'Antunes', 955512334, '1989-03-30', 'Rua Nova 95', 'M', '2000',458215631,4),
						   ('Maria', 'S', 'Varges', 854423168, '1997-02-10', 'Rua Pirilan 75', 'F', '1500',985545752,5),
						   ('Marcelo', 'N', 'Morais', 995223115, '1982-05-15', 'Rua C 185', 'M', '1700',325521563,2),
						   ('Lidia', 'V', 'Pestana', 633588521, '1990-11-20', 'Rua da Usina 159', 'F', '5000',954872230,2),
						   ('Vinicius', 'N', 'Gomes', 775333254, '1972-08-14', 'Rua Machado', 'M', '3500',335548221,3);
                           
insert into dependent values (955512334, 'Alice', 'F', '1986-04-05', 'Daughter'),
							 (955512334, 'Theodore', 'M', '1983-10-25', 'Son'),
                             (955512334, 'Joy', 'F', '1958-05-03', 'Spouse'),
                             (955512334, 'Abner', 'M', '1942-02-28', 'Spouse'),
                             (854423168, 'Michael', 'M', '1988-01-04', 'Son'),
                             (854423168, 'Alice', 'F', '1988-12-30', 'Daughter'),
                             (775333254, 'Elizabeth', 'F', '1967-05-05', 'Spouse');

insert into departament values ('Research', 5, 633588521, '2015-05-22'),
							   ('Administration', 4, 854423168, '2010-01-01'),
                               ('Headquarters', 1, 995223115,'1999-06-19');

insert into dept_locations values (1, 'Houston'),
								 (4, 'Stafford'),
                                 (5, 'Bellaire'),
                                 (5, 'Sugarland'),
                                 (5, 'Houston');

insert into project values ('ProductX', 1, 'Bellaire', 5),
						   ('ProductY', 2, 'Sugarland', 5),
						   ('ProductZ', 3, 'Houston', 5),
                           ('Computerization', 10, 'Stafford', 4),
                           ('Reorganization', 20, 'Houston', 1),
                           ('Newbenefits', 30, 'Stafford', 4)
;

insert into works_on values (775333254, 1, 32.5),
							(854423168, 2, 7.5),
                            (633588521, 3, 40.0),
                            (995223115, 2, 20.0),
                            (633588521, 2, 10.0),
                            (775333254, 3, 10.0),
                            (852649731, 10, 10.0),
                            (852649731, 20, 10.0),
                            (852649731, 30, 30.0),
                            (854423168, 10, 10.0),
                            (633588521, 10, 35.0),
                            (854423168, 30, 5.0),
                            (955512334, 30, 20.0),
                            (995223115, 20, 15.0),
                            (775333254, 20, 0.0);
                            
-- Usando query para retornar valores

select * from employee;

-- gerente e seu departamento
select ssn, fname, dname from employee e, departament d where (e.ssn = d.mgr_ssn);

-- recuperando dependentes dos empregados
select fname, dependent_name, relationship from employee, dependent where essn = ssn;

-- retornando valores pelo nome
select bdate, address from employee where fname= 'Wendell' and minit= 'B' and lname='Pestana';

-- recuperando departamento especifico
select * from departament where dname='Research';

select fname, lname, address from employee, departament where dname='Research' and dnumber=dno;

--
select pname, essn, fname, hours from project, works_on, employee where pnumber = pno and essn = ssn;


