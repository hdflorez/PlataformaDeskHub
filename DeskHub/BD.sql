CREATE DATABASE DESKHUB
USE DESKHUB;
CREATE TABLE ROLES
(IdRol int not null primary key identity(1,1),
NombreRol varchar(500) not null,
EstadoRol bit not null)
 
CREATE TABLE USUARIOS
(IdUsuario int not null primary key identity(1,1),
TipoUsuario varchar(50) not null,
Identificacion varchar(50) not null,
Nombre varchar(500) not null,
correo varchar(1000) not null,
EstadoUsuario bit not null)

CREATE TABLE USUARIO_ROL
(Id int not null primary key identity(1,1),
FkIdRol int not null,
FkIdUsuario int not null,
constraint FkRoles foreign key(FkIdRol) references ROLES(IdRol),
constraint FkUsuarios foreign key(FkIdUsuario) references USUARIOS(IdUsuario))

CREATE TABLE UBICACION
(IdUbicacion int not null primary key identity(1,1),
Nombre varchar(255) not null,
EstadoUbicacion bit not null)

CREATE TABLE ASIENTOS
(IdAsiento int not null primary key identity(1,1),
FkUbicacion int not null,
CodigoAsiento varchar(50) not null,
Nombre varchar(100) not null,
EstadoAsiento bit not null,
constraint FkUbicacion foreign key(FkUbicacion) references UBICACION(IdUbicacion))

CREATE TABLE TIPO_JORNADA
(IdTipoJornada int not null primary key identity(1,1),
Nombre varchar(100) not null,
EstadoTipoJornada bit not null)

CREATE TABLE RESERVAS(
IdReserva int not null primary key identity(1,1),
FkTipoJornada int not null,
FkAsientos int not null,
FkUsuario int null,
FechaCreacion date not null,
FechaReserva date not null,
HoraReserva varchar(5) not null,
EstadoReserva bit not null,
constraint FkTipoJornada foreign key(FkTipoJornada) references TIPO_JORNADA(IdTipoJornada),
constraint FkAsientos foreign key(FkAsientos) references ASIENTOS(IdAsiento))