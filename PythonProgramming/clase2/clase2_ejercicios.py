"""
lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

i=0
for cad in lista:
    lista[i]= lista[i].title()
    i+=1
print(lista)
"""

"""
def capitalizar(lista):
    resultado= []

    for nombre in lista:
        
        nombre_apellido = nombre.split()
        if len(nombre_apellido) == 2:
            nombre, apellido = nombre_apellido
            nombre = nombre.capitalize()
            apellido = apellido.capitalize()
            nombre_capitalizado = f"{nombre} {apellido}"
            resultado.append(nombre_capitalizado)

    return resultado

lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

resultado = capitalizar(lista)

print(resultado)
"""

"""
lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

def mayusculas(lista):
    contador = 0
    nueva = []

    while contador < len(lista):
        separador = lista[contador].split()
        auxiliar = separador[0].capitalize() + " " + separador[1].capitalize()
        nueva.append(auxiliar)
        contador += 1

    print(nueva)


mayusculas(lista)
"""
