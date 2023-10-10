# CONEXION A BASES DE DATOS

# MySQL <-- mysql-connector-python, PyMySQL, MySQLdb
# PostgreSQL --> psycopg, pg8000
# SQLite <-- sqlite3
# SQL Server --> pymssql, pyodbc
# Oracle --> cx_Oracle

# SQLite

# Browser --> https://sqlitebrowser.org
"""
import sqlite3

# Variable donde guarda la BBDD
dir = "C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\Clases\\clase4\\"

# Crear una conexión con la BBDD
conn = sqlite3.connect(dir + "database.sqlite")

# Crear cursor
cursor = conn.cursor()

# Correr código SQL con el método execute()
try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")
except sqlite3.OperationalError:
    print("La tabla ya existe!")

cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad)) # FORMA CORRECTA

# Realizamos un commit() para confirmar los cambios
conn.commit()

# Finalizamos la conexión
conn.close()
"""

# MySQL (Structured Query Language - Lenguaje de Consulta Estructurado)


# Abrir XAMPP
# Para crear un usuario, abrir un CMD, ir donde está instalado XAMPP

# cd \xampp\mysql\bin
# mysql -u root

# 1 - Crear un nuevo usuario
# CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'nueva_contraseña';

# 2 - Concederle privilegios
# GRANT ALL PRIVILEGES ON *.* TO 'nuevo_usuario'@'localhost';

# 3 - Actualizamos para que los cambios surtan efecto
# FLUSH PRIVILEGES;

# 4 - Crear una BBDD
# CREATE DATABASE nueva_base_de_datos;

# 5 - Dar privilegios al usuario sobre la BBDD
# GRANT ALL PRIVILEGES ON nueva_base_de_datos.* TO 'nuevo_usuario'@'localhost';

# 6 - Actualizamos para que los cambios surtan efecto
# FLUSH PRIVILEGES;

# Instalamos pymysql
# pip install pymysql

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    passwd="admin",
    db="digitalers"
)

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE personas (nombre VARCHAR(50), edad INT)")
except pymysql.err.OperationalError:
    print("La tabla ya existe!")

gente = (
    ("Pablo", 30),
    ("Jorge", 41),
    ("Pedro", 27)
)

#for nombre, edad in gente:
#    cursor.execute("INSERT INTO personas VALUES (%s, %s)", (nombre, edad))

conn.commit()

try:
    cursor.execute("SELECT * FROM personas")
except pymysql.err.ProgrammingError:
    print("Error en la consulta SQL. Validar la sintaxis")

datos = cursor.fetchall()
print(datos)

conn.close()