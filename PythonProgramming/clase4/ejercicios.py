import sqlite3

"""
Desarrollar un programa que cree una base de datos SQLITE3 llamada productos.sqlite y una tabla de nombre productos con las siguientes columnas.

Columna	Tipo de Dato
id	NUMERIC
nombre	TEXT
precio	NUMERIC

Luego el programa debe insertar las siguientes filas

id	nombre	precio
1	Teclado	25
2	Mouse	18
3	Monitor	300
4	Pad	100

"""

"""
dir = "C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\Clases\\clase4\\"
conn = sqlite3.connect(dir + "productos.sqlite")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")
except sqlite3.OperationalError:
    print("La tabla ya existe!!")


cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (1, "Teclado", 25))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (2, "Mouse", 18))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (3, "Monitor", 300))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (4, "Pad", 100))


conn.commit()
conn.close()
"""

"""
Realizar un programa que permita agregar nuevos productos a la base anterior a través de la consola. Se debe solicitar para cada producto un id (numerico), un nombre (texto) y un precio (numérico). 

Menu
1 - Agregar Productos
2 - Ver productos
3 - Salir

La opcion 1 despliega la entrada de datos
La opcion 2  muestra los productos de la tabla
La 3 nos permite salir del programa (sys.exit() o break)
"""
dir = "C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\Clases\\clase4\\"
conn = sqlite3.connect(dir + "productos.sqlite")
cursor = conn.cursor()

def menu():
    print("===========Menu==========")
    print("1 - Agregar Productos")
    print("2 - Ver productos")
    print("3 - Salir")
    print("=========================")

def agregar_productos():
    print(">>>>Ingresar producto<<<<")
    id = int(input("Ingrese el id del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))

    cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (id, nombre, precio))
    print("Los datos se ingresaron correctamente")

def ver_productos():
    print(">>>>Ver productos<<<<")
    cursor.execute("SELECT * FROM productos")
    productos_db = cursor.fetchall()
    print(productos_db)


while True:
    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        agregar_productos()
    elif opcion == 2:
        ver_productos()
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion incorrecta")


conn.commit()
conn.close()