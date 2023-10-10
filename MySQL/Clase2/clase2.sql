/*
Consultas con lenguaje SQL
--------------------------

Para iniciar consultas usando lenguaje SQL usamos la cláusula SELECT.
Podemos combinarla con otras cláusulas:

- FROM: Especifica la tabla de la cual queremos obtener registros
SELECT * FROM conciertos;
SELECT Band, City FROM conciertos;

Realizo una operación matemática y muestro el resultado en una nueva columna.
Le agregamos 21% de impuesto a EntrancePrice

SELECT *, EntrancePrice * 1.21 AS 'FinalPrice' FROM conciertos;

Podemos usar Aliases para visualizar los nombres de los campos de otra forma temporalmente.

SELECT Band, ConcertName AS Concert, EntrancePrice AS Price FROM conciertos;
*/


/*
- WHERE: Especifica condiciones que tienen que cumplir los registros que vamos a buscar

SELECT Band, Location FROM conciertos WHERE Location = 'Mercedes-Benz Arena Berlin';

*/


/*
- GROUP BY: Agrupa registros seleccionados en función de uno o más campos. A veces se usa en conjunto
con funciones de agregación, como SUM(), COUNT(), MIN(), MAX(), AVG()

SELECT Band, Country, City, Location, EntrancePrice AS Price, SUM(TicketsSold) AS TotalSold FROM conciertos GROUP BY City;


- HAVING: Especifica condiciones que tienen que cumplir los grupos generados

SELECT Band, Country, City, Location, EntrancePrice AS Price, SUM(TicketsSold) AS TotalSold FROM conciertos GROUP BY City HAVING TotalSold > 200;
*/

/*
- ORDER BY: Ordena los registros seleccionados en función de un campo

SELECT * FROM conciertos ORDER BY Band; --> Ordena los registros por orden alfabético y de manera ascendente

SELECT * FROM conciertos ORDER BY Band DESC; --> Ordena de manera descendente

*/


/*
LIMIT
-----

Limita el número de filas que se van a devolver en una consulta.
Se puede usar junto a la cláusula OFFSET que lo que hace es cambiar la posición desde donde se hace
la consulta. En el ejemplo que sigue, el OFFSET 3 saltea los 3 primeros registros y trae los 2 
siguientes.

SELECT Band FROM conciertos LIMIT 2 OFFSET 3;

*/

/*
LITERALES
---------

Son cadenas alfanuméricas que podemos agregar en una columna aparte cuando hacemos una consulta.

SELECT <selección>, <VALOR> <NOMBRE_COLUMNA> FROM <TABLA>
SELECT *, 'Concert Confirmed' Status FROM conciertos;

*/

/*
ORDEN DE LAS CLÁUSULAS
----------------------

1) FROM
2) WHERE
3) GROUP BY
4) HAVING
5) ORDER BY

*/

/*
OPERACIONES DE COMPARACIÓN
--------------------------

Operador    Descripción
--------    -----------
=           Igual a
<           Menor que
>           Mayor que
>=          Mayor o igual que
<=          Menor o igual que
<>          No es igual a

OPERADORES LOGICOS
------------------

Operador    Descripción
--------    -----------
AND         Se deben cumplir todas las condiciones especificadas
OR          Se debe cumplir al menos una de las condiciones especificadas
NOT         No se debe cumplir la condición especificada


- Si uno o más valores a comparar son NULL, el resultado es NULL
- El operador <=> funciona igual que el operador =, excepto que si en la comparación una o
las dos expresiones son NULL, el resultado no es NULL. Si comparamos 2 expresiones NULL el resultado
es true.

SELECT * FROM conciertos WHERE City = 'Berlin' AND EntrancePrice < 100;


OPERADORES BETWEEN y NOT BETWEEN
--------------------------------

Se usan para ver si una expresión está comprendida entre 2 rangos de valores:

SELECT * FROM conciertos WHERE EntrancePrice BETWEEN 100 AND 200;

SELECT * FROM conciertos WHERE TicketsSold NOT BETWEEN 70 AND 200;


OPERADORES IN y NOT IN
----------------------

Validan si el valor de una expresión se encuentra dentro, o no, de un conjunto indicado

SELECT * FROM conciertos WHERE Country IN ('France');

SELECT * FROM conciertos WHERE Country NOT IN('France', 'United Kingdom');


OPERADORES LIKE y NOT LIKE
--------------------------

Se utilizan para hacer comparaciones entre cadenas y patrones. Trae resultados si la cadena
se ajusta al patrón, caso contrario no trae nada.
Si la cadena o el patron es NULL, el resultado es NULL

% --> Busca coincidencias con cualquier número de caracteres

SELECT * FROM conciertos WHERE City LIKE '%erli%';

_ --> Busca coincidencia con un único caracter por guión

SELECT * FROM conciertos WHERE City LIKE '_erli%';

El caso de NOT LIKE es el opuesto

A tener en cuenta:

- LIKE no distingue entre mayúsculas y minúsculas
- Si la cadena de por sí ya incluye símbolos porcentuales o guines bajos, necesitaríamos usar
secuencias de escape para especificar que se debe respetar ese caracter tal cual está.

SELECT * FROM conciertos WHERE City LIKE '%\_del\_%';

En este ejemplo la ciudad es "Mar_del_Plata". Usamos secuencias de escape para que los guiones bajos
los tome como parte de la cadena y no como caracteres a reemplazar.


OPERADORES IS NULL e IS NOT NULL
--------------------------------

Sirven para verificar si una expresión determinada es o no nula

SELECT * FROM conciertos WHERE City IS NOT NULL;

*/