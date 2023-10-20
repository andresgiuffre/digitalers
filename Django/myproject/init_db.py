import sqlite3

conn = sqlite3.connect("cursos.db")
cursor = conn.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE cursos (nombre TEXT, inscripciones NUMERIC)")
conn.commit()

clases = (
    ("Python", 10),
    ("Java", 12),
    ("PHP", 8)
)

for clase, estudiantes in clases:
    cursor.execute("INSERT INTO cursos VALUES (?, ?)", (clase, estudiantes))

conn.commit()
conn.close()