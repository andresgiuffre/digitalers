-- FUNCIONES INTEGRADAS
   --------------------

-- CONCAT() Concatena strings en una sola columna

SELECT CONCAT('Concert at ', City, ', ', Country) 'Concert Location' FROM conciertos;

-- CONCAT_WS() Concatena strings pero su primer argumento es el caracter que se va a usar como separador

SELECT CONCAT_WS(', ', Band, City, Country) 'Datos' FROM conciertos;

-- UPPER() Convierte el valor del campo en letras mayúsculas.

SELECT UPPER(Country) as País FROM conciertos;

-- LOWER() Convierte el valor del campo en letras minúsculas

SELECT LOWER(Country) as País FROM conciertos;

-- LEFT() Obtiene los primeros caracteres de un string

SELECT CONCAT(LEFT(Band, 1), '.') as 'Primer Letra Banda' FROM conciertos;

-- RIGHT() Obtiene los últimos caracteres de un string

SELECT RIGHT(Location, 5) as 'Ultimas Letra Ubicacion' FROM conciertos;

-- SUBSTRING() Extrae una cantidad de caracteres a partir de una posición que le pasamos

-- Argumento 1: El campo en el que queremos extraer una cadena
-- Argumento 2: La posición a partir de la cual empezamos a extraer caracteres (esta posición está
-- incluida en la extracción)
-- Argumento 3: La cantidad de caracteres a extraer como una nueva cadena

SELECT SUBSTRING(LocationAddress, 4, 5) as Direccion FROM conciertos;

-- CHAR_LENGTH() Cuenta la cantidad de caracteres que hay en una cadena

SELECT Country, CHAR_LENGTH(Country) as 'Cantidad de Letras' FROM conciertos;

-- LOCATE() Devuelve a partir de qué número de caracter comienza una cadena que le pasemos

SELECT Band, LOCATE('Will', Band) as 'Posición' FROM conciertos;

-- LTRIM() Elimina espacios en blanco al inicio de una cadena

SELECT LTRIM(City) as Ciudad FROM conciertos;

-- RTRIM() Elimina espacios en blanco al final de una cadena

SELECT RTRIM(City) as Ciudad FROM conciertos;

-- TRIM() Elimina espacios de ambos lados de la cadena

SELECT TRIM(City) as Ciudad FROM conciertos;

-- REPLACE() Reemplaza una cadena de caracteres por otra

SELECT REPLACE(ConcertName, 'Concert', 'In Concert') as Concierto FROM conciertos;


-- FUNCIONES DE FECHA
   ------------------

-- YEAR() Extrae el año de un campo de fecha

SELECT YEAR(Date) as 'Año' FROM conciertos;

-- MONTH() Extrae el mes de un campo de fecha

SELECT MONTH(Date) as 'Mes' FROM conciertos;

-- DAY() Extrae el día de un campo de fecha

SELECT DAY(Date) as 'Día' FROM conciertos;

-- HOUR() Extrae la hora de un campo datetime (fecha/hora)

SELECT HOUR(Date) as 'Hora' FROM conciertos;

-- MINUTE() Extrae los minutos de un campo datetime (fecha/hora)

SELECT MINUTE(Date) as 'Minutos' FROM conciertos;

-- SECOND() Extrae los segundos de un campo datetime (fecha/hora)

SELECT SECOND(Date) as 'Segundos' FROM conciertos;

-- CURDATE() Devuelve la fecha actual

SELECT CURDATE() as 'Fecha Actual';

-- CURTIME() Devuelve la hora actual

SELECT CURTIME() as 'Hora Actual';

-- DATEDIFF() Calcula la cantidad de días que pasan entre 2 fechas

SELECT DATEDIFF(CURDATE(), Date) as 'Dias Transcurridos' FROM conciertos WHERE Band = 'Ozzy Osbourne';

-- TIMESTAMPDIFF() Calcula la cantidad de meses o años que transcurren entre 2 fechas

SELECT TIMESTAMPDIFF(MONTH, '2023-01-27', '2023-04-30') as 'Meses';

SELECT TIMESTAMPDIFF(YEAR, '2018-01-27', CURDATE()) as 'Años';

-- DAYNAME() Devuelve el nombre el día en un campo de fecha

SELECT DAYNAME(CURDATE()) as 'Nombre del día';

SELECT Date, Band, DAYNAME(Date) as 'Nombre del día' from conciertos;

-- DAYOFWEEK() Devuelve el número del día de la semana, siendo Domingo el día número 1

SELECT DAYOFWEEK(CURDATE()) as 'Número de día';

-- DAYOFYEAR() Devuelve el número del día del año

SELECT DAYOFYEAR(CURDATE()) as 'Número de día del año';

-- MONTHNAME() Devuelve el nombre del mes de un campo fecha

SELECT MONTHNAME(CURDATE()) as 'Nombre del mes';

-- ADDDATE() Suma un valor a un tipo de campo fecha de una determinada cantidad de días,
-- meses o años.

-- La función lleva como primer argumento la fecha inicial, y como 2do argumento un intervalo en
-- días, meses o años que se le van a sumar a la fecha inicial.

SELECT CURDATE() as 'Fecha Actual',
ADDDATE(CURDATE(), INTERVAL 2 MONTH) as 'Vencimiento a 2 meses',
ADDDATE(CURDATE(), INTERVAL 90 DAY) as 'Vencimiento a 90 días',
ADDDATE(CURDATE(), INTERVAL 2 YEAR) as 'Vencimiento a 2 años';


