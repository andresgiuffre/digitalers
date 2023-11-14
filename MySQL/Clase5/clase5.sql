-- SUBCONSULTAS

-- Se trata de una consulta SELECT dentro de otra consulta SELECT

SELECT * FROM libros WHERE libro_id IN (SELECT libro_id FROM libroautor);

-- Nos devuelve 25 resultados (libroautor tiene 25 registros y libros tiene 26 registros)

-- SUBCONSULTA ESCALAR
-- Es la subconsulta que devuelve resultados únicos como sumas, promedios, valores mínimos, máximos, etc

SELECT * FROM libros WHERE precio > (SELECT AVG(precio) FROM libros);

SELECT * FROM libros WHERE precio > (SELECT MAX(cantidad) FROM ventas);

SELECT * FROM libros WHERE LEFT(titulo, 1) = (SELECT LEFT(apellido, 1)
FROM empleados WHERE puesto_id = 2);

-----------------------------------------------------

-- CONDICIONAL CASE

-- Evalúa diversas consultas y realiza acciones si la condición se cumple.
-- Con WHEN determinamos la condición y con THEN lo que ocurre
-- La cláusula ELSE se usa cuando ninguna condición se cumple
-- CASE finaliza siempre con END

SELECT titulo, precio,
CASE
	WHEN precio < 10 THEN 'Barato'
    WHEN precio BETWEEN 15.50 AND 25 THEN 'Equilibrado'
    ELSE 'Caro'
END AS Categoría
FROM libros;


SELECT libro_id, forma_pago, cantidad,
CASE
	WHEN cantidad > 30 AND (forma_pago = 'Efectivo' OR forma_pago = 'Transf') THEN 'Excelente'
    WHEN cantidad > 30 AND forma_pago = 'Cheque' THEN 'Muy buena'
    WHEN cantidad > 20 AND (forma_pago = 'Efectivo' OR forma_pago = 'Transf') THEN 'Buena'
    WHEN cantidad > 10 AND (forma_pago = 'Efectivo' OR forma_pago = 'Transf') THEN 'Regular'
    ELSE 'Mala'
END as 'Tipo de Venta'
FROM ventas ORDER BY cantidad DESC;

-----------------------------------------------------

-- UNION

-- consulta1 UNION [ALL] consulta2;

-- Compara resultados de 2 o más consultas y los combina en un nuevo resultado basado en
-- la comparación.
-- En cada resultado tienen que existir la misma cantidad de campos
-- Los campos que se comparen tienen que ser del mismo tipo de datos

SELECT nombre, apellido FROM autores
UNION
SELECT nombre, apellido FROM empleados;


SELECT CONCAT(nombre, ' ', apellido) as nombre, provincia
FROM autores WHERE provincia = 'CF'
UNION
SELECT nombre, provincia FROM editoriales;


SELECT CONCAT(nombre, ' ', apellido) as nombre, provincia
FROM autores WHERE provincia = 'ER'
UNION ALL
SELECT nombre, provincia FROM editoriales;

---------------------------------------

-- Producto cartesiano entre tablas
-- Combina todos los elementos de una tabla con todos los elementos de la otra

SELECT * FROM productos, marcas;

-- Composicion interna: Es un producto cartesiano restringido por un condicional.
-- Hacemos que los elementos se emparejen 

SELECT * FROM productos, marcas
WHERE productos.Marca = marcas.idMarca;

-------------------------------------------------

-- CROSS JOIN
-- Hace una especie de producto cartesiano y el resultado muestra las combinaciones
-- de todas las filas de las 2 tablas. Se puede aplicar sobre la misma tabla.


SELECT * FROM selecciones as L 
CROSS JOIN selecciones as V
WHERE L.EQUIPO <> V.EQUIPO
ORDER BY L.EQUIPO;


-- Inner Join
-- Combina 2 o más tablas basándose en un campo en común. La condición de unión
-- se marca con la cláusula ON

SELECT * FROM clientes
INNER JOIN pedidos
ON clientes.COD_CLIENTE = pedidos.CODIGO_CLIENTE
ORDER BY COD_CLIENTE;

-- Left Join
-- Devuelve los registros de la tabla de la izquierda y los que coinciden con los de la derecha

SELECT * FROM clientes
INNER JOIN pedidos
ON clientes.COD_CLIENTE = pedidos.CODIGO_CLIENTE
ORDER BY COD_CLIENTE;

-- Si queremos ver solo la parte izquierda sin la parte central (o sea, solo clientes que NO
-- hayan hecho pedidos)

SELECT * FROM clientes
LEFT JOIN pedidos
ON clientes.COD_CLIENTE = pedidos.CODIGO_CLIENTE
WHERE NUMERO_PEDIDO IS NULL
ORDER BY COD_CLIENTE;


-- Right Join
-- Devuelve los registros de la tabla de la derecha y los que coinciden con los de la izquierda

SELECT * FROM clientes
RIGHT JOIN pedidos
ON clientes.COD_CLIENTE = pedidos.CODIGO_CLIENTE
WHERE COD_CLIENTE IS NULL
ORDER BY COD_CLIENTE;

-----------------------------------------
-- FOREIGN KEY
-- Con ON DELETE y ON UPDATE declaramos que lo que ocurra con los elementos de la tabla padre (Articulos)
-- (updates o deletes) afectan también a los relacionados de la tabla hija (Facturas)

CREATE TABLE Facturas(Letra char not null, Numero int, id_articulo int UNSIGNED not null,
PRIMARY KEY (Letra, Numero));

CREATE TABLE Articulos(id_articulo int unsigned not null auto_increment, Nombre varchar(30) not null,
PRIMARY KEY (id_articulo));

ALTER TABLE Facturas ADD FOREIGN KEY(id_articulo) REFERENCES
Articulos(id_articulo) 
ON DELETE CASCADE
ON UPDATE CASCADE;

---------------------------------------
-- Superllave
-- Es la suma de uno o más campos que permiten identificar registros de manera única
-- Ej: en una tabla de Estudiantes, si tenemos ID, nombre, apellido, email, combinando el ID
-- y el email ya tenemos una manera única de identificar al estudiante.



