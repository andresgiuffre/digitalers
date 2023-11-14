'''
Utilizando la tabla LIBROS (base de la librería) obtener una lista de todos los productos 
cuyo precio supere el precio promedio de todos los libros. La lista debe contener todos
los campos de la tabla. Ordenar alfabéticamente por título
'''

SELECT * FROM libros
WHERE precio > (SELECT AVG(precio) FROM libros)
ORDER BY titulo;

'''
Extraer de la tabla libros una lista de todos los que pertencen a la categoría Novelas
cuyo precio sea superior al libro más caro de la categoría Ensayos. Ordenar de mayor
a menor por precio de los libros
'''

SELECT * FROM libros
WHERE categoria = 'NOVELAS' AND
precio > (SELECT MAX(precio) FROM libros
WHERE categoria = 'Ensayos')
ORDER BY precio DESC;

'''
A partir de la tabla Empleados, extraer una lista de todos aquellos empleados con el
puesto más alto
'''

SELECT * From empleados
WHERE puesto_id = (SELECT MAX(puesto_id)
FROM EMPLEADOS);

'''
En la tabla Libros, generar una consulta que muestre los campos libro_id, titulo, categoria y
precio.
Agregar una columna con el nombre TIPO en la que se muestren los valores solicitados.
Menor a 15 es ECONOMICO, menor o igual a 30 es REGULAR, el resto es DELUXE.
Ordenar alfabeticamente el resultado por título. No se debe mostrar en el resultado
aquellos libros que no tienen precio (falta de stock)
'''

SELECT libro_id, titulo, categoria, precio,
CASE
	WHEN precio < 15 THEN 'ECONOMICO'
    WHEN precio <= 30 THEN 'REGULAR'
    ELSE 'DELUXE'
END as TIPO
FROM libros
WHERE precio IS NOT NULL
ORDER BY titulo;

'''
Generar una consulta que muestre las siguientes columnas: libro_id, titulo, precio, local_id,
factura_nro y cantidad. Estos campos están en las tablas libros y ventas. Ordenar alfabéticamente
el resultado por los titulos
'''

SELECT V.libro_id, titulo, precio, local_id, factura_nro, cantidad
FROM libros as L, ventas as V
WHERE L.libro_id = V.libro_id
ORDER BY L.titulo;

'''
Crear una consulta en la que se muestren solo los títulos de aquellos libros que nunca
hayan sido vendidos. Ordenar alfabéticamente
'''

SELECT L.titulo from libros as L
LEFT JOIN ventas as V
ON L.libro_id = V.libro_id
WHERE factura_nro IS NULL
ORDER BY titulo;