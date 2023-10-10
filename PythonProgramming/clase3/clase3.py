# CLASES Y OBJETOS

"""
class MiClase:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def imprimir_edad(self):
        print(self.edad)


mi_objeto = MiClase("Juan", 34)
mi_objeto.imprimir_edad()
"""

"""
class OperacionesMatematicas:
    def __init__(self, numero):
        self.numero = numero


    def sumar(self, nro2):
        self.numero += nro2
        print(self.numero)


    def restar(self, nro2):
        self.numero -= nro2
        print(self.numero)


    def multiplicar(self, nro2):
        self.numero *= nro2
        print(self.numero)


mi_objeto = OperacionesMatematicas(10)
mi_objeto.sumar(5)
mi_objeto.restar(4)
mi_objeto.multiplicar(2)
mi_objeto.sumar(3)

otro_objeto = OperacionesMatematicas(3)
otro_objeto.sumar(8)
"""

# ENCAPSULAMIENTO

# Getters, Setters y Del

"""
class Clase:
    def __init__(self):
        self.__atributo = "Atributo Oculto"

    
    def get_atributo(self): # Getter
        return self.__atributo
    

    def set_atributo(self, valor): # Setter
        self.__atributo = valor


    def eliminar_atributo(self): # Del
        del self.__atributo


    def __saludo_privado(self):
        print("Hola!!, este es un saludo privado")


    def saludo_publico(self):
        self.__saludo_privado()
"""

# HERENCIA

# La clase Base, padre o superclase que contiene métodos y atributos que otras clases van a heredar
# La clase Derivada, hija o subclase que va a hereder métodos y atributos del padre.

"""
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas


class ClaseA:
    def __init__(self):
        self.a = 1

    def mensaje(self):
        print("Mensaje de la Clase A")


class ClaseB:
    def __init__(self):
        self.a = 2

    def mensaje(self):
        print("Mensaje de la clase B")


class ClaseC(ClaseA, ClaseB):
    def mensaje(self):
        print("Mensaje clase C") # Sobreescritura
        super().mensaje()

    def mensaje_b(self):
        ClaseB.mensaje(self)


mi_objeto = ClaseC()
mi_objeto.mensaje() # Imprime mensaje ClaseC y ClaseA que es el primer padre
mi_objeto.mensaje_b() # Imprime mensaje de ClaseB
"""

# POLIMORFISMO

"""
class Perro:
    def sonido(self):
        return "Guau!"
    

class Gato:
    def sonido(self):
        return "Miau!"
    

def sonido_del_animal(animal):
    return animal.sonido()

perro = Perro()
gato = Gato()

print(sonido_del_animal(perro))
print(sonido_del_animal(gato))
"""

"""
import math

class Figura:
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio


    def calcular_area(self):
        return math.pi * self.radio ** 2
    

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def calcular_area(self):
        return self.base * self.altura
    

# Creo las instancias de las subclases
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

# Calcular el área de diferentes figuras usando polimorfismo
def calcular_y_mostrar_area(figura):
    area = figura.calcular_area()
    print(f"El área de la figura es: {area}")


calcular_y_mostrar_area(circulo)
calcular_y_mostrar_area(rectangulo)
"""

# MODULOS Y PAQUETES

# La gran mayoria de los modulos externos están listados en PYPI (Python Package Index)
# pypi.org

# Para instalar paquetes externos usamos pip

# pip install <nombre_del_paquete> --> Instala un paquete
# pip uninstall <nombre_del_paquete> --> para desinstalar
# pip freeze --> Nos lista los paquetes que están instalados
# pip search <termino_de_busqueda> --> Para buscar paquetes en PyPI


# ARGUMENTOS DE PROGRAMA

# Librería sys - sys.argv (es una lista)
# Sirve en caso de ejecutar el script desde un terminal

"""
import sys

nombres = sys.argv[1:]

if nombres:
    for nombre in nombres:
        print(f"Hola, {nombre}!!")
else:
    print("No indicaste ningún nombre!")
"""

# SISTEMA DE ARCHIVOS

"""
# Librería os
import os

# Funcion os.listdir() --> Devuelve una lista con archivos y carpetas contenidos en el directorio
dir = os.listdir("C:\\Temp")
print(os.listdir(os.getcwd()))
print(dir)

# os.path.exists() --> Valida si carpeta o archivo existen y devuelve un booleano
exists = os.path.exists("C:\\Temp")
print(exists)

# os.mkdir() --> Crea una carpeta
try:
    os.mkdir("C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\demo")
except FileExistsError:
    print("La carpeta ya existe!!")

# os.rmdir() --> Elimina una carpeta siempre que se encuentre vacía
try:
    os.rmdir("C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\demo")
except OSError:
    print("El directorio no está vacío!!")

# os.remove() --> Elimina un archivo
try:
    os.remove("C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\demo\\temporal.txt")
except FileNotFoundError:
    print("No se encuentra el archivo")

# os.rename() --> Renombramos archivos
try:
    os.rename("C:\\Temp\\a.py", "C:\\Temp\\b.py")
except FileNotFoundError:
    print("No se encuentra el archivo")

# os.system --> ejecuta comandos del SO
os.system("dir")

# os.name --> Nos informa que SO estamos corriendo. nt = Windows, posix = Linux
print(os.name)

# SHUTIL

import shutil

# shutil.copy() --> Copia archivos de una carpeta origen a una destino
directorio = "C:\\Temp"
try:
    shutil.copy(directorio + "\\b.py", directorio + "\\c.py")
except FileNotFoundError:
    print("El archivo ya no existe!")

# shutil.move() --> Mueve un archivo de un lado a otro
try:
    shutil.move(directorio + "\\b.py", directorio + "\\d.py")
except FileNotFoundError:
    print("El archivo no existe!")

# shutil.rmtree() --> Elimina una carpeta con todo el contenido que tenga
shutil.rmtree("C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\demo2")

# *** CUIDADO AL BORRAR PORQUE NO SE RECUPERAN EN LA PAPELERA!!!! ***
"""

# EJECUCION DE COMANDOS CON subprocess

import subprocess

"""
lista = ["mkdir", "Carpeta Nueva"]
resultado = subprocess.run(lista, shell=True)

if  resultado.returncode == 0:
    print("La carpeta fue creada con éxito")
else:
    print("Hubo un error al crear la carpeta")
"""

host = subprocess.run("hostname", capture_output=True, encoding="cp850")
print(host.stdout.strip())

host = subprocess.run(["python", "--version"], capture_output=True, encoding="cp850")
print(host.stdout.strip())
