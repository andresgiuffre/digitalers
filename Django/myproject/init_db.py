import sqlite3

dir = 'C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\EducacionIT\\Django\\myproject\\'
conn = sqlite3.connect(dir + "cursos.db")
cursor = conn.cursor()

# Crear una tabla
#cursor.execute("CREATE TABLE cursos (nombre TEXT, inscripciones NUMERIC)")
cursor.execute("CREATE TABLE cine (nombre TEXT, fecha_estreno TEXT, edad_minima NUMERIC, preventa_online BOOLEAN)")
#cursor.execute("SELECT * FROM cine")
#conn.commit()

#clases = (
#    ("Python", 10),
#    ("Java", 12),
#    ("PHP", 8)
#)

#for clase, estudiantes in clases:
#    cursor.execute("INSERT INTO cursos VALUES (?, ?)", (clase, estudiantes))

conn.commit()
conn.close()