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



*/