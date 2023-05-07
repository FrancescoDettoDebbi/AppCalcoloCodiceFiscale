create database if not exists catastale;
use catastale;
create table comuni(
	codice char(4) primary key not null,
  comune varchar(255) not null
);
