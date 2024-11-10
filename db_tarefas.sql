create database db_tarefas;
use db_tarefas;

create table tbl_usuarios (
	id int not null primary key auto_increment,
    nome varchar(255) not null,
    email varchar(255) not null
);

create table tbl_tarefas (
	id int not null primary key auto_increment,
    descricao varchar(255) not null,
    setor varchar(255) not null,
    prioridade varchar(255) not null,
    tar_status varchar(255) not null,
    tar_data date not null
);

ALTER TABLE tbl_tarefas
ADD constraint fk_id_usuarios
foreign key (id) references tbl_usuarios(id);

SELECT * FROM db_tarefas.tbl_tarefas;

SELECT * FROM db_tarefas.tbl_usuarios;
