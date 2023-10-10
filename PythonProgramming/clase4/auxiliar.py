# VULNERABILIDAD EN SQLITE3

"""
import sqlite3

dir = "C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\Clases\\clase4\\"
conn = sqlite3.connect(dir + "productos.sqlite")
cursor = conn.cursor()

def insertar():
    gente = (
        ("Pablo", 30),
        ("Jorge", 41),
        ("Pedro", 27)
    )

    try:
        for nombre, edad in gente:
            cursor.execute(f"INSERT INTO personas VALUES ('{nombre}', {edad})")
    except sqlite3.OperationalError:
        print("Error al insertar datos!")


def consultar():
    try:
        cursor.execute("SELECT * FROM productos")
        personas_db = cursor.fetchall()
        return personas_db
    except sqlite3.OperationalError:
        return "La tabla no existe!"
    

def ingreso_de_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # *** ESTAS LINEAS PERMITEN INYECCION DE CODIGO SQL ***
    #cursor.executescript(f"INSERT INTO personas VALUES ('{nombre}', {edad})")
    #cursor.executescript("INSERT INTO personas VALUES ('{}', {})".format(nombre, edad))
    #cursor.executescript("INSERT INTO personas VALUES ('" + nombre + "', " + str(edad) + ")")

    cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad)) # FORMA CORRECTA
    print("Los datos se ingresaron correctamente!")


#ingreso_de_usuario()
print(consultar())

conn.commit()

conn.close()
"""

# VULNERABILIDAD EN MySQL

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    passwd="admin",
    db="digitalers",
    client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
)

cursor = conn.cursor()

def ingreso_datos():
    try:
        cursor.execute("CREATE TABLE personas (nombre VARCHAR(50), edad INT)")
    except pymysql.err.OperationalError:
        print("La tabla ya existe!")

    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    cursor.execute("INSERT INTO personas VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    print("Se ingresaron los datos correctamente")
    conn.close()


def consultar_datos():
    cursor.execute("SELECT * FROM personas")

    datos = cursor.fetchall()
    print(datos)
    conn.close()


#ingreso_datos()
consultar_datos()