-- Introducción a las BBDD

-- Oracle
-- MySQL
-- SQL Server 
-- PostgreSQL
-- SQLite

-- SQL (Structured Query Language)

-- CRUD: Create, Read, Update, Delete


/*
Sentencias SQL
--------------

DDL (Data Definition Language)

- CREATE: Sirve para crear tablas nuevas, vistas, indices, etc
- ALTER: Modificar la estructura existente en la base. (Agregar, modificar, eliminar columnas, etc)
- DROP: Eliminar tablas, vistas, indices de la base de datos
- TRUNCATE: Elimina los registros de una tabla, pero mantiene la estructura (los campos)

DML (Data Manipulation Language)

- SELECT: Recupera datos de una o mas tablas
- INSERT: Agrega nuevos registros a la tabla
- UPDATE: Modifica registros de una tabla
- DELETE: Elimina registros de la tabla

DCL (Data Control Language)

- GRANT: Otorga privilegios de accesos a usuarios o roles
- REVOKE: Revoca privilegios de acceso

TCL (Transaction Control Language)

- COMMIT: Confirma la transacción actual, guardando los cambios en la base
- ROLLBACK: Deshace la transacción actual, revirtiendo los cambios realizados
- SAVEPOINT: Establece un punto de control dentro de la transacción y establece hasta donde se 
pueden deshacer los cambios con un Rollback

*/

/*
CONCEPTOS PRELIMINARES
----------------------

Tablas - Almacena los datos, tienen un nombre único dentro de la base.

Tipos de datos:

Cadenas de Texto

- CHAR: Almacena cadenas de longitud fija, entre 1 y 255 caracteres. CHAR ocupa en la base el máximo de
longitud asignado. 
- VARCHAR: Idem CHAR, pero de longitud variable. Almacena en la base solamente lo que ocupe el dato
- TINYTEXT: Texto de longitud variable que puede tener hasta 255 caracteres
- TEXT: idem anterior, pero puede contener hasta 65.535 caracteres
- MEDIUMTEXT: idem anterior, pero contiene hasta 16.777.215
- LONGTEXT: idem anterior, contiene hasta 4.294.967.295
- BLOB: Datos binarios que pueden almacenar archivos o textos. Los tipos TINYBLOB, BLOB, MEDIUMBLOB,
LONGBLOB, son identicos a sus pares TEXT. La busqueda de BLOBs es case sensitive.


Datos Numéricos

Nota: Los datos de tipo INT admiten atributos SIGNED y UNSIGNED. El primero admite valores negativos
y el segundo sólo positivos.

- BIT o BOOL: Se usa para un número entero que puede ser 0 ó 1
- TINYINT: Número entero con rango de valores de entre -128 y 127. Unsigned va de 0 a 255
- SMALLINT: idem anterior -32.768 a 32.767. Con Unsigned va de 0 a 65.535
- MEDIUMINT: idem anterior -8.388.608 a 8.388.607. Unsigned de 0 a 16.777.215
- INT: idem -2.147.463.848 a 2.147.463.647. Unsigned va de 0 a 4.294.967.295
- BIGINT: idem -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807. Unsigned de 0 
a 18.446.744.073.709.551.615
- FLOAT (m, d): Son números con decimales. La "m" representa el número TOTAL de dígitos (incluyendo
decimales) y la "d" cuenta cuántos decimales va a tener de ese total. (ej: FLOAT(5,2) = 516.20)
- DOUBLE: idem anterior, abarcando un mayor rango numérico
- DECIMAL: Almacena números como cadenas de texto

Campos de Fecha

- DATE: Almacena fechas. El formato por defecto es YYYY-MM-DD
- DATETIME: Combina fecha y hora. El formato por defecto es año-mes-día horas:minutos:segundos
- TIME: Almacena una hora. El formato que usa es HH:MM:SS
- YEAR: Almacena un año. El rango permitido va desde 1901 hasta 2155. Este campo puede tener un
tamaño de entre 2 ó 4 dígitos

*/

/*
Creación de una base de datos

CREATE DATABASE <nombre_de_la_base>;

Creación de una tabla

CREATE TABLE productos(
	idProducto INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(50) NOT NULL,
    Precio DOUBLE,
    Marca VARCHAR(30) NOT NULL,
    Categoria VARCHAR(30) NOT NULL,
    Stock INT(6) UNSIGNED NOT NULL,
    Disponible BOOLEAN DEFAULT false
);


Atributos para los campos:

- UNIQUE: Indica que la columna no puede tener valores repetidos (email VARCHAR(50) UNIQUE;)
- UNSIGNED: Permite almacenar solo valores positivos
- ZERO_FILL: Siempre que el campo sea numérico, autocompleta los numeros faltantes con ceros. 
(factura INT(5) ZERO_FILL;) --> factura 1 ---> 00001
- AUTO_INCREMENT: Incrementa automáticamente el valor numérico del campo. Se utiliza únicamente con
la columna que sea Primary Key


Eliminar una tabla

DROP TABLE <nombre_de_la_tabla>;

DROP TABLE IF EXISTS <nombre_de_la_tabla>;

OTROS COMANDOS SQL
------------------

SHOW DATABASES; --> Nos muestra un listado de bases creadas

USE <nombre_de_la_base>; --> Nos posiciona en una determinada base para poder utilizarla

SHOW TABLES; --> Muestra un listado de tablas de la base que estemos usando

DESCRIBE <nombre_de_tabla> --> Devuelve detalles sobre la estructura de la tabla

*/

/*
CONCEPTOS AVANZADOS
-------------------

ENUM

Se usa para definir un conjunto de valores constantes y fijos para una columna.
La columna solo puede tener una serie de valores que se los especificamos al crear la tabla y 
solamente se podrán usar esos valores para esa columna.

CREATE TABLE usuarios(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    dni INT UNSIGNED NOT NULL,
    estado_civil ENUM('soltero/a', 'casado/a', 'divorciado/a', 'viudo/a')
);


SET

Similar a ENUM pero en un campo SET se pueden seleccionar varios elementos de la lista.

CREATE TABLE otros_productos(
	id INT PRIMARY KEY,
    nombre VARCHAR(50),
    caracteristicas SET('Resistente al agua', 'Duradero', 'Ecológico', 'Ligero')
);

*/

/*
MODIFICACION DE ESTRUCTURAS
---------------------------

ALTER TABLE:

Agregar una columna

ALTER TABLE productos ADD COLUMN Color VARCHAR(15) NULL AFTER Categoria;

Si le pongo FIRST la ubica en primer lugar. Si no le pongo nada, la ubica en último lugar.

Cambiar nombre de columna:

ALTER TABLE productos CHANGE Color Vendidos VARCHAR(50) NULL;

Cambiar tipo de dato de una columna:

ALTER TABLE productos MODIFY Vendidos INT UNSIGNED NOT NULL DEFAULT 0;

Eliminar una columna:

ALTER TABLE productos DROP COLUMN Vendidos;

Renombrar una tabla:

1) ALTER TABLE otros_productos RENAME productos2;

2) RENAME TABLE productos2 TO otros_productos;

Eliminar la restricción de PRIMARY KEY:

ALTER TABLE productos DROP PRIMARY KEY;

Si el campo de PK tiene la propiedad AUTO_INCREMENT, debemos quitarla antes de eliminar el PK:
Modificamos todo el campo sin la propiedad AUTO_INCREMENT.

ALTER TABLE productos MODIFY idProducto INT UNSIGNED NOT NULL;

Agregar la Primary Key:

ALTER TABLE productos ADD PRIMARY KEY(idProducto)

Agregar nuevamente el AUTO_INCREMENT:

ALTER TABLE productos MODIFY idProducto INT UNSIGNED AUTO_INCREMENT NOT NULL;


FOREIGN KEY (Clave Foránea)
---------------------------

La Foreign Key estable una relación entre 2 tablas. Enlaza una columna de una tabla con la columna
que lleva la Primary Key en la otra tabla.

CREATE TABLE Clientes (
	ID INT auto_increment PRIMARY KEY,
    Nombre VARCHAR(50)
);

CREATE TABLE Pedidos (
	ID INT auto_increment PRIMARY KEY,
    ClienteID INT,
    Producto VARCHAR(50),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID)
);

Para ver la Foreign Key (buscar el nombre del CONSTRAINT):

SHOW CREATE TABLE pedidos;

Eliminar Foreign Key:

ALTER TABLE pedidos DROP FOREIGN KEY pedidos_ibfk_1;

Dar de alta una Foreign Key:

ALTER TABLE pedidos ADD CONSTRAINT pedidos_ibfk_1 FOREIGN KEY(ClienteID) REFERENCES Clientes(ID);


INSERCIÓN DE DATOS
------------------

Manera completa de inserción de datos:

Se especifica la tabla, cada uno de los campos y sus valores

INSERT INTO productos(Nombre, Precio, Marca, Categoria, Stock, Disponible) VALUES ('iPhone', 499.99, 'Apple', 'Smartphone', 500, false);

Manera SQL:

INSERT INTO productos
SET Nombre = 'Edge 30 Pro', Precio = 399.99, Marca = 'Motorola', Categoria = 'Smartphone', Stock = 300, Disponible = true;

Manera simplificada:

Se debe respetar el orden de los campos cuando vayamos a ingresar los valores. El primer valor que
le pasamos es el del Primary Key, puede ser NULL o 0. Este valor será ignorado y entra en vigor el
AUTO_INCREMENT.

INSERT INTO productos
VALUES (NULL, 'S23', 450, 'Samsung', 'Smartphone', 240, true);

*/
