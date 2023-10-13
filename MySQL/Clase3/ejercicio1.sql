-- EJERCICIO:

-- 1) Crear una base de datos llamada Kiosco y posicionarse en esa base

CREATE DATABASE kiosco;
USE kiosco;

-- 2) Crear una tabla llamada productos que tenga estos elementos:

/*
ID - Enteros positivos no nulos que se incrementen automáticamente y que sirva como key
Nombre - cadena de caracteres para nombrar el producto
Precio - Campo numérico con decimales para el precio
Stock - Número entero positivo para llevar control de stock
*/

CREATE TABLE productos (
    ID INT UNSIGNED AUTO_INCREMENT NOT NULL,
    Nombre VARCHAR(255),
    Precio DECIMAL(10, 2),
    Stock INT UNSIGNED,
    PRIMARY KEY (ID)
);

-- 3) Llenar esa tabla con 3 o 4 registros inventados

INSERT INTO productos (Nombre, Precio, Stock) VALUES
    ('Caramelos de goma', 50.00, 500),
    ('Galletitas Fantoche', 600, 20),
    ('Papel Absorbente', 800, 10),
    ('Yerba CBSe', 900, 5);
    
-- 4) Realizar dos consultas, una para ver todos los registros y otra para ver los que haya un stock de 10 productos o menos

SELECT * FROM productos;
SELECT * FROM productos WHERE Stock <= 10;

-- 5) Cambiar el nombre del campo Stock por Inventario

ALTER TABLE productos CHANGE Stock Inventario INT UNSIGNED;

-- 6) Actualizar el precio de un producto y actualizar el inventario de otro producto para dejarlo en 0

UPDATE productos SET Precio = 50.25 WHERE ID = 1;
UPDATE productos SET Inventario = 0 WHERE ID = 2;

-- 7) Crear una segunda tabla llamada sin_inventario con los campos:

/*
ID - entero positivo no nulo incremental primary key
Nombre - Nombre del producto
*/

CREATE TABLE sin_inventario (
    ID INT UNSIGNED AUTO_INCREMENT NOT NULL,
    Nombre VARCHAR(255),
    PRIMARY KEY (ID)
);

-- 8) Pasar los registros con inventario 0 a la nueva tabla, solo incluyendo los campos ID y Nombre

INSERT INTO sin_inventario (ID, Nombre) SELECT ID, Nombre FROM productos WHERE Inventario = 0;
SELECT * FROM sin_inventario;

-- 9) Eliminar un producto de la primer tabla e insertar uno totalmente nuevo

DELETE FROM productos WHERE ID = 2;
INSERT INTO productos (Nombre, Precio, Inventario) VALUES ('Rocklets', 210.39, 85);

-- 10) Hacer una consulta de todos los registros de la primer tabla y usar un alias para que en lugar de mostrar la columna inventario la muestre con el nombre Stock
-- 11) Hacer una consulta de todos los registros de la primer tabla y ordenar los valores por precio
-- 12) Hacer una consulta de todos los registros de la tabla y mostrar solo el 2do y 3er elemento
-- 13) Mostrar los productos que tengan precio entre 50 y 100 (o los valores que quieran)