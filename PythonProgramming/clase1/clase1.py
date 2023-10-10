"""
PYTHON
------
"""

enteros = 10
punto_flotante = 5.8
cadenas = "Hola"
booleanos = True
complejos = 2 + 6j # Consultar librería CMATH

# Casting - Convertir variable de un tipo a otro

a = 10
b = 2.5
resultado = a + b

# Colecciones

# LISTAS

#lista = [1, 2, 3, 4, 5]
        #0, 1, 2, 3, 4
       #-5,-4,-3,-2,-1

animales = ['perro', 'gato', 'conejo', 'hamster', 'vaca', 'leon']
#print(animales[2:5]) # SLICES --> ['conejo', 'hamster', 'vaca']

#print(animales[0:5:2]) # El tercer parámetro es el paso al que 
                        # reproduce la secuencia (de 2 en 2)
                        # ['perro', 'conejo', 'vaca']

lista = [10, 5.4, False, ["otra lista", True]]

#print(lista[1])
#print(lista[3])
#print(lista[3][0])

#lista[2] = "Hola"

lista.append('otro elemento') # --> [10, 5.4, False, ['otra lista', True], 'otro elemento']
lista.insert(1, 12) # --> [10, 12, 5.4, False, ['otra lista', True], 'otro elemento']

# TUPLAS

tupla = (1, 2, 3, 4)

un_elemento = (5,)

# DICCIONARIOS

diccionario = {'a': 1, 'b': 2}

diccionario2 = {1: 'uno', 2: 'verdadero', (1, 2): 'tupla', False: 'dos'}

diccionario2[1] = '1' # Modifica un elemento
diccionario2[3] = 'tres' # Crea un elemento al final del diccionario
del diccionario2[3] # Elimina un elemento a través de su key
#print(diccionario2)

# SET y FROZENSET

#SET 
lista_repetida = [1, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8]
set1 = set(lista_repetida) # --> {1, 2, 3, 4, 5, 6, 7, 8}

# FROZENSET --> una vez definido no se puede modificar

frutas = frozenset(["manzana", "banana", "cereza"])

# len() y del

# con del elimino elementos, con len() conozco la longitud de una colección

# UNPACKING - desempaquetado
# Asigno elementos de una tupla o lista en variables
a, b, c, d = tupla

#print(a, b, c, d)

# OPERADORES ARITMETICOS

suma = 5 + 6
resta = 10 - 2
multiplicacion = 2 * 4
division = 10 / 2
modulo = 9 % 2
exponencial = 2 ** 3
division_entera = 9 // 2

# OPERADORES RELACIONALES

x = 5

x == 6 # Evalua Igualdad - False
x != 8 # Evalua Diferencia - True
x > 4 # True
x < 3 # False
x >= 20 # False
x <= 5 # True

# OPERADORES LOGICOS

x == 6 and x == 5 # Devuelve True si ambos elementos son True
x == 6 or x == 5 # Devuelve True si al menos un elemento es True
not x > 4 # Devuelve el contrario, si a era True me deuvelve False y viceversa

# OPERADOR DE IDENTIDAD (is)

a = 10
b = 10

a is b # Devuelve True ya que apuntan a la misma direccion de memoria

# OPERADOR DE MEMBRESIA (in)

datos = [1, 2, 3]
3 in datos # Devuelve True porque 3 es miembro de datos
10 in datos # Devuelve False porque 10 no es miembro de datos

# OPERADOR WALRUS (Morsa) :=
# Simplifica la operación de asignación. Crea una variable, le asigna el valor y ejecuta
# lo que tenga que ejecutar al mismo tiempo.

#dato = "hola"
#print(dato)

#print(dato:="Hola")


# SENTENCIAS DE CONTROL

"""
nombre = "Juan"

if nombre == 'Pedro':
    print('Tu nombre es Pedro')
else:
    print('Tu nombre no es Pedro, sino ' + nombre)
"""

# OPERADOR TERNARIO
# Resultado de evaluacion exitosa - condición - else - resultado de evaluación no exitosa

edad = 19

#print("La edad es de 18 años" if edad == 18 else "La edad no es de 18 años, sino " + str(edad))

# ELIF
"""
edad = 80

if edad < 18:
    print('Sos menor de edad')
elif edad < 65:
    print('Sos mayor de edad')
else:
    print('Ya estás jubilado')


numero = 0

if numero:
    print('El número es ' + str(numero))
else:
    print('FALSO, el número es 0')
"""

# BUCLE WHILE

a = 1

while a < 3:
    #print(a)
    a += 1

# BUCLE FOR

datos = [1, 2, 3, 4]

#for dato in datos:
#    print(dato)

# BREAK y CONTINUE
"""
#WHILE
contador = 0

while True:
    print("Este es el paso", contador)
    contador += 1

    if contador >= 5:
        print("La condición se cumple, salimos del bucle")
        break


#CONTINUE
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        print("Saltando la iteración cuando contador sea 3")
        continue

    print("Este es el paso", contador)
"""

# FUNCIONES BUILT-IN

#print() input() range()

# A range le puedo pasar hasta 3 parámetros. El primero es el inicio de secuencia. El 2do es
# el final de la secuencia, el cual ese mismo número es excluido, y el 3er parámetro es el paso
# de la secuencia (ej: de 2 en 2)

#for numero in range(2, 10, 2):
    #print(numero)

lista_pares = list(range(2, 11, 2))
#print(lista_pares)

# int() float() str() len() min() max() bool()

# FUNCIONES

def sumar(a, b):
    c = a + b
    

#print(sumar(10, 20))

def imprimir_mensajes(mensaje="No se escribió nada"):
    """
    Esta función sirve para impimir mensajes,
    si no se le pasa ningún parámetro, devolverá un mensaje
    por defecto.
    """
    print(mensaje)

#help(imprimir_mensajes)
#imprimir_mensajes()

# SCOPE

x = 1

def funcion():
    global x
    x = 2

#print(x)
funcion()
#print(x)

def funcion_externa():
    z = 'hola'

    def funcion_interna():
        nonlocal z
        z = 'chau'

    funcion_interna()
    #print(z)


# ARGUMENTOS DE LONGITUD VARIABLE

def funcion(*args):
    #print(type(args))
    #print(args)
    pass


#funcion(1, 2, 3, 4, 5, 6, 7)

def suma(**kwargs):
    #print(type(kwargs))
    #print(kwargs)

    total = 0
    for arg in kwargs:
        total = total + kwargs[arg]
    #print(total)


suma(a=10, b=20, c=30, d=40, e=77)

# ORDEN DE LOS ARGUMENTOS DE LAS FUNCIONES

def funct(a, b, *args, c='hola', **kwargs):    
    pass

