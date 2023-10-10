"""
class Persona():
    
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = int(edad)
    
    def cumpleanio(self):
        self.edad += 1
        print(f"Hola, soy {self.nombre} y tengo {self.edad}")


sebastian = Persona("Sebastian", 40)
sebastian.cumpleanio()
"""

"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1
        print(f"Soy {self.nombre} y ahora tengo {self.edad} años.")

aumentar_edad = Persona("Carolina", 30)
aumentar_edad.cumpleanios()
"""

"""
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumpleanios(self):
        self.edad +=1
        print(self.edad)
            
persona1= Persona ("ana", 20)
persona1.cumpleanios()
"""

"""
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    
    def nombre_completo(self):
        print(f"{self.nombre} {self.apellido}")


class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera, edad):
        super().__init__(nombre, apellido)
        self.carrera = carrera
        self.edad = edad

    def mostrar_carrera(self):
        print(f"{self.apellido} {self.nombre}, {self.edad} años, estudiante de {self.carrera}")

estudiante1 = Estudiante("Juan", "Perez", "Ingeniería en Informática", 25)
estudiante1.mostrar_carrera()
estudiante1.nombre_completo()
"""

# EJERCICIO RUTA Y EXTENSIONES

import os
import sys

# Pasamos los argumentos y validamos que haya la cantidad correcta
ruta = sys.argv[1]
extension = sys.argv[2]
if not ruta and not extension:
    print("La cantidad de argumentos no es la correcta. Deben ser 2")
    sys.exit()

# Obtener una lista de archivos en la ruta
try:
    validar_contenido = os.listdir(ruta)
except FileNotFoundError:
    print("La ruta no existe")
    sys.exit()


for contenido in validar_contenido:
    if contenido.endswith(extension):
        print(contenido)
    else:
        print(f"No se encuentrar archivos con la extensión {extension}")
        sys.exit()