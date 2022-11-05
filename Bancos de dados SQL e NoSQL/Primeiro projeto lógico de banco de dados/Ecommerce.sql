-- Criação do banco de dados para o cenário de E-commerce
-- drop database ecommerce;
create database ecommerce;
use ecommerce;

-- Criar tabela cliente
create table clients(
	idClient int auto_increment primary key,
	Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(255),
    constraint unique_cpf_client unique (CPF)
);

alter table clients auto_increment = 1;

-- Criar tabela produto
create table product(
	idProduct int auto_increment primary key,
	Pname varchar(45),
    Classification bool default false,
    Category enum('Eletrônico', 'Vestimenta', 'Brinquedos','Alimentos', 'Moveis') not null,
    Avaliation float default 0,
    Size varchar(10)
);


-- Para ser continuado no desafio: termine de implementar a tabela e crie a conexão com as tabelas necessárias
-- além disso, reflita essa modificação no diagrama de esquema relacional
-- Criar constraints relacionadas ao pagamento

-- Tabela de pagamento não teve relacionamento com nenhuma outra sendo uma tabela isolada, não cadastrada
-- create table payments(
	-- idclient int,
    -- idpayment int,
    -- typePayment enum('Boleto', 'Cartão', 'Dois Cartões'),
    -- limitAvailable float, 
    -- primary key(idclient, idPayment)
-- ):

-- Criar tabela pedido
create table orders(
	idOrder int auto_increment primary key,
    idOrderClient int,
    orderStatus enum('Cancelado', 'Confirmado','Em processamento') default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    paymentCash bool default false,
    constraint fk_orders_client foreign key (idOrderClient) references clients(idClient)
);


-- Criar tabela estoque
create table productStorage(
	idProdStorage int auto_increment primary key,
    storageLocation varchar(255),
    quantity int default 0
);

-- Criar tabela fornecedor
create table supplier(
	idSupplier int auto_increment primary key, 
    SocialName varchar(255) not null,
    CNPJ char(15) not null,
    contact char(11) not null,
    constraint unique_supplier unique (CNPJ)
);

-- Criar tabela vendedor
create table seller(
	idSeller int auto_increment primary key, 
    SocialName varchar(255) not null,
    AbstName varchar(255),
    CNPJ char(15),
    CPF char(9),
    location varchar(255),
    contact char(11) not null,
    constraint unique_cnpj_seller unique (CNPJ),
    constraint unique_cpf_seller unique (CPF)
);

-- Criar relacionamento produto_vendedor
create table productSeller(
	idPseller int,
    idPproduct int,
    prodQuantity int default 1,
    primary key (idPseller, idPproduct),
    constraint fk_product_seller foreign key(idPseller) references seller(idSeller),
    constraint fk_product_product foreign key(idPproduct) references product(idProduct)
);


-- Criar relacionamento produto_pedido
create table productOrder(
	idPOproduct int,
    idPOorder int,
    poQuantity int default 1,
    poStatus enum('Disponivel', 'Sem estoque') default 'Disponivel',
    primary key (idPOproduct, idPOorder),
    constraint fk_productOrder_seller foreign key(idPOproduct) references product(idProduct),
    constraint fk_productOrder_product foreign key(idPOorder) references orders(idOrder)
);

-- Criar relacionamento Localização_estoque
create table storageLocation(
	idLproduct int,
    idLstorage int,
	location varchar(255) not null,
    primary key (idLproduct, idLstorage),
    constraint fk_storageLocation_seller foreign key(idLproduct) references product(idProduct),
    constraint fk_storageLocation_product foreign key(idLstorage) references productStorage(idProdStorage)
);

-- Criando relacionamento produto_pedido
create table productSupplier(
	idPsSupplier int,
    idPsProduct int,
    quantity int not null,
    primary key (idPsSupplier, idPsProduct),
    constraint fk_productSupplier_supplier foreign key(idPsSupplier) references supplier(idSupplier),
    constraint fk_productSupplier_product foreign key(idPsProduct) references product(idProduct)
);

show tables;

