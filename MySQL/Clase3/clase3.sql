/*
UPDATE
------

UPDATE <nombre_tabla>
SET <campo_x> = <valor_x> WHERE <campo> = <valor>;

Ejemplo:

UPDATE conciertos
SET EntrancePrice = 120 WHERE Band = 'Ozzy Osbourne';

Si se requiere desactivar medida de seguridad:

SET SQL_SAFE_UPDATES = 0; ---> El valor en 0 desactiva, en 1 activa

Se puede modificar más de 1 registro a la vez:

UPDATE conciertos
SET EntrancePrice = 185, TicketsSold = 218
WHERE ConcertName = 'Metropolis';

-----------------------------------------------------------------

DATOS ANEXADOS
--------------

Podemos pasar datos de una tabla a otra con una sola sentencia:

Creamos una nueva tabla:

CREATE TABLE conciertos_suspendidos (
	BandID INT UNSIGNED NOT NULL auto_increment PRIMARY KEY,
    Band VARCHAR(50) NOT NULL,
    ConcertName VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    TicketsSold INT
);

Agregamos una columna a la tabla original:

ALTER TABLE conciertos ADD COLUMN Suspended BOOLEAN default false;

Marcamos un concierto como suspendido

UPDATE conciertos
SET Suspended = true WHERE Band = 'Hans Zimmer Live';

Pasamos los datos de los conciertos suspendidos de la tabla original
a la nueva tabla.

INSERT INTO conciertos_suspendidos (BandID, Band, ConcertName, City, TicketsSold) 
SELECT BandID, Band, ConcertName, City, TicketsSold FROM conciertos
WHERE Suspended = true;

------------------------------------------------

ELIMINAR REGISTROS
------------------

DELETE FROM conciertos_suspendidos WHERE BandID = 5;

Para borrar TODOS los registros de una tabla:

DELETE FROM <tabla>;

Truncate elimina todos los registro de la tabla y resetea los valores del AUTO_INCREMENT 
(DELETE no lo hace)

TRUNCATE TABLE <tabla>;

----------------------------------------------------

FUNCIONES MATEMATICAS INTEGRADAS
--------------------------------

ROUND()

Funcion que sirve para redondear valores numéricos.

SELECT ROUND(EntrancePrice) FROM conciertos WHERE Band = 'Elton John';

Podemos redondear una operacion matemática y asignarle que solo mantenga 2 decimales.
SELECT ROUND(EntrancePrice/3,2) FROM conciertos;


CEIL()

Devuelve el resultado de una operación matemática redondeado hacia arriba.

SELECT EntrancePrice, EntrancePrice * 1.21 AS 'Precio + IVA', CEIL(EntrancePrice * 1.21) AS 'Precio Redondeado' 
FROM conciertos;


FLOOR()

Devuelve el resultado de una operación pero redondeado hacia abajo.

SELECT EntrancePrice, EntrancePrice * 1.21 AS 'Precio + IVA', FLOOR(EntrancePrice * 1.21) AS 'Precio Redondeado' 
FROM conciertos;


MOD()

Devuelve el resto de una división entre números

SELECT MOD(15, 4);
SELECT MOD(EntrancePrice, 2) FROM conciertos;


POW()

Eleva un número a una determinada potencia. (Ejemplo, 2 al cubo)

SELECT POW(2, 3);
SELECT POW(TicketsSold, 1/2) FROM conciertos; --> Saco raiz cuadrada de los Tickets vendidos

----------------------------------------------------------------

FUNCIONES DE AGREGADO
---------------------

COUNT()

Devuelve una cantidad de valores que tengamos en un campo específico

Devuelve la cantidad de registros
SELECT COUNT(*) FROM conciertos;

Podemos agregarle condiciones para filtrar la búsqueda
SELECT COUNT(*) FROM conciertos WHERE Country = 'Germany';


SUM()

Devuelve una suma de valores

SELECT SUM(TicketsSold) FROM conciertos WHERE City LIKE '%erli%';


MIN()

Nos devuelve el valor mínimo relacionado a la búsqueda que se realice

SELECT MIN(EntrancePrice) AS 'Valor Mínimo' from conciertos;


MAX()

Nos devuelve el valor máximo de la búsqueda

SELECT MAX(EntrancePrice) AS 'Valor Máximo' from conciertos;


AVG()

Devuelve un promedio del campo numérico que le especifiquemos

SELECT AVG(TicketsSold) FROM conciertos WHERE City = 'Berlin';


GROUP BY

SELECT Country, City, SUM(TicketsSold) AS TotalSold, AVG(EntrancePrice) AS AveragePrice 
FROM conciertos GROUP BY City;

SELECT Country, City, SUM(TicketsSold) AS TotalSold, AVG(EntrancePrice) AS AveragePrice 
FROM conciertos GROUP BY City HAVING AveragePrice < 200;


*/