create database if not exists company_constraints;
use company_constraints;
create table employee(
	fname varchar(20) not null,
    minit char,
    lname varchar(20) not null,
    ssn char(9) not null,
    bdate date,
    address varchar(45),
    sex char,
    salary decimal(10,2),
    super_snn varchar(40),
    dno int not null,
    constraint chk_salary_employee check (salary> 2000.0),
    constraint pk_employee primary key (ssn)
);

create table departament(
	dname varchar(40) not null,
    dnumber int not null, 
    mgr_ssn char(9),
    mgr_start_date date,
    primary key (dnumber),
    unique (dname),
    foreign key (mgr_ssn) references employee(ssn)
);

create table dept_locations(
	dnumber int not null,
    dlocation varchar(15) not null,
    primary key (dnumber, dlocation),
    foreign key (dnumber) references departament (dnumber)
);

create table project(
	pname varchar(15) not null,
    pnumber int not null,
    plocation varchar(15),
    dnum int not null,
    primary key (pnumber),
    unique (pname),
    foreign key (dnum) references dept_locations (dnumber)
);

create table works_on(
	essn char(9) not null,
    pno int not null,
    hours decimal(3,1),
    primary key (essn, pno),
    foreign key (essn) references employee (ssn),
    foreign key (pno) references project(pnumber)
);

create table dependent(
	essn char(9) not null,
    dependent_name varchar(15) not null, 
    sex char,
    bdate date,
    relationship varchar(8), 
    primary key (essn, dependent_name),
    foreign key (essn) references employee (ssn)
);

show tables;
desc dependent;







