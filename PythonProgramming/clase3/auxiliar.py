from clase3 import Automovil, ClaseA, ClaseB


"""
mi_objeto = Clase()

print(mi_objeto.get_atributo()) # Probamos el Getter

mi_objeto.set_atributo("Cambio de Valor") # Probamos el Setter
print(mi_objeto.get_atributo())

mi_objeto.eliminar_atributo() # Probamos el Del

try:
    print(mi_objeto.get_atributo())
except AttributeError:
    print("Ese atributo ya no está disponible")


mi_objeto.saludo_publico()


mi_objeto._Clase__saludo_privado()
mi_objeto._Clase__atributo = "Te acabo de hackear el atributo"
print(mi_objeto._Clase__atributo)
"""

# Creamos una instancia de la clase Automovil
mi_auto = Automovil("Toyota", "Corolla", 4)

# Acceder a los atributos de la clase base 
print("Marca:", mi_auto.marca)
print("Modelo:", mi_auto.modelo)
print("Puertas:", mi_auto.puertas)