'''
Generar una lista en la que se muestren todos los artistas y las canciones de la tabla spotify.
El nombre de cada artista y el título de la canción deben mostrarse separados con un guión en
una columna llamada CANCION
Ordenar la lista resultante de forma alfabética por la columna CANCION
Además mostrar el campo GENERO
'''

SELECT CONCAT(ARTISTA, ' - ', TITULO) as CANCION, GENERO FROM spotify ORDER BY CANCION;

'''
Misma consulta usando la función CONCAT_WS
'''

SELECT CONCAT_WS(' - ', ARTISTA, TITULO) as CANCION, GENERO FROM spotify ORDER BY CANCION; 

'''
Misma consulta pero con la columna GENERO en mayúsculas
'''

SELECT CONCAT_WS(' - ', ARTISTA, TITULO) as CANCION, UPPER(GENERO) as GENERO 
FROM spotify ORDER BY CANCION;

'''
Agregar a la consulta anterior una columna con el nombre AÑOS en la que se calcule la cantidad
de años transcurridos desde que se lanzó cada una de las canciones al año actual
'''

SELECT CONCAT_WS(' - ', ARTISTA, TITULO) as CANCION, UPPER(GENERO) as GENERO, YEAR(CURDATE()) - YEAR(ANIO) as AÑOS 
FROM spotify ORDER BY CANCION;

'''
Generar una consulta que calcule la cantidad de registros que figuran en la tabla Spotify.
El resultado debe mostrarse en una columna con el nombre CANCIONES
'''

SELECT COUNT(*) as CANCIONES from spotify;

'''
Generar una consulta que muestre la cantidad de canciones lanzadas al mercado por año
'''

SELECT YEAR(ANIO) as AÑO, COUNT(*) as CANCIONES FROM spotify GROUP BY AÑO;

'''
Modificar la consulta anterior para no mostrar aquellos años en los que se hayan lanzado
menos de 50 canciones
'''

SELECT YEAR(ANIO) as AÑO, COUNT(*) as CANCIONES FROM spotify GROUP BY AÑO HAVING CANCIONES >= 50;

----------------------------------------------------------------------------

'''
Crear una BBDD con el nombre LIBRERÍA. Poner en uso la base generada. La misma está conformada por
8 tablas.

Una vez creadas las tablas, insertar un conjunto de registros en cada una de ellas utilizando
el archivo con el nombre SCRIPT
'''

CREATE DATABASE LIBRERÍA;

USE LIBRERÍA;

CREATE TABLE autores(
    autor_id varchar(11),
    apellido varchar(40),
    nombre varchar(20),
    telefono varchar(12),
    direccion varchar(40),
    ciudad varchar(20),
    provincia char(2),
    c_postal char(5),
    estado tinyint(1)
);

CREATE TABLE ventas(
    local_id char(4),
    factura_nro varchar(20),
    fecha datetime,
    cantidad smallint,
    forma_pago varchar(12),
    libro_id varchar(6)
);

CREATE TABLE locales(
 local_id char(4),
 nombre varchar(40),
 direccion varchar(40),
 ciudad varchar(20),
 provincia char(2),
 c_postal char(5)
);


CREATE TABLE editoriales(
 editorial_id char(4),
 nombre varchar(40),
 ciudad varchar(20),
 provincia char(2),
 pais varchar(30)
);


CREATE TABLE libros(
 libro_id varchar(6),
 titulo varchar(80),
 categoria char(12),
 editorial_id char(4),
 precio double,
 comentarios varchar(200),
 fecha_publicacion datetime
);


CREATE TABLE libroautor(
 autor_id varchar(11),
 libro_id varchar(6)
);


CREATE TABLE puestos(
 puesto_id smallint,
 descripcion varchar(50)
);

CREATE TABLE empleados(
    empleado_id char(9),
    nombre varchar(20),
    apellido varchar(30),
    puesto_id smallint,
    editorial_id char(4),
    fecha_ingreso datetime
);

'''
Utilizar la BBDD Librería y generar una lista en la que se muestren todos los autores y la
provincia en la que nacieron.
El apellido y el nombre de cada autor debe mostrarse separados por una coma y un espacio en una columna 
llamada AUTOR.
Ordenar alfabéticamente los apellidos resultantes
'''

SELECT CONCAT(apellido, ', ', nombre) as autor, provincia from autores ORDER BY autor;

'''
Modificar la consulta anterior para obtener el mismo resultado con CONCAT_WS
'''

SELECT CONCAT_WS(', ', apellido, nombre) as autor, provincia from autores ORDER BY autor;

'''
Misma consulta pero mostrando los nombres de los autores en mayúsculas
'''

SELECT UPPER(CONCAT_WS(', ', apellido, nombre)) as autor, provincia from autores ORDER BY autor;

'''
Misma consulta pero mostrar únicamente la inicial del nombre del autor y su apellido
'''

SELECT UPPER(CONCAT(apellido, ', ', LEFT(nombre, 1), '.')) as autor, provincia 
from autores ORDER BY autor;

'''
Generar una columna con el nombre INGRESO en la que se muestren todos los empleados y el año
en el que ingresaron a trabajar a la empresa. El apellido y nombre de cada empleado se
mostrarán separados con una coma y un espacio en una columna con el nombre EMPLEADO.
Ordenar de mayor a menor segun los años de ingreso de cada empleado.
'''

SELECT CONCAT(APELLIDO, ', ', NOMBRE) AS EMPLEADO, 
YEAR(FECHA_INGRESO) AS INGRESO FROM EMPLEADOS ORDER BY INGRESO DESC;

'''
Modificar la consulta anterior para agregar una columna con el nombre ANTIGUEDAD. Debe
calcular la cantidad de años de antigüedad de cada empleado dentro de la empresa al día de
hoy
'''

SELECT CONCAT(APELLIDO, ', ', NOMBRE) AS EMPLEADO, 
YEAR(FECHA_INGRESO) AS INGRESO, TIMESTAMPDIFF(YEAR, FECHA_INGRESO, CURDATE()) AS ANTIGUEDAD 
FROM EMPLEADOS ORDER BY INGRESO DESC;

'''
Generar una consulta para obtener el precio mas bajo de la tabla LIBROS. El resultado se debe
mostrar en una columna con el nombre MENOR PRECIO
'''

SELECT MIN(precio) as 'Menor Precio' FROM libros;

'''
Misma consulta pero que agregue el precio más alto de la tabla. La columna se debe llamar
Mayor Precio
'''

SELECT MIN(precio) as 'Menor Precio', MAX(precio) as 'Mayor Precio' FROM libros;

'''
Calcular el precio más bajo, más alto y el precio promedio de los libros pertenecientes a 
cada categoría
'''

SELECT CATEGORIA, MIN(precio) as 'Menor Precio', MAX(precio) as 'Mayor Precio', ROUND(AVG(precio), 2) AS 'Precio Promedio' 
FROM libros;

