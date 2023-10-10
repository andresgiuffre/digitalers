import requests


def obtener_datos():
    response = requests.get("http://localhost:7001/student")
    print("Código de Estado:", response.status_code)
    respuesta = response.json()
    print("Contenido de la respuesta:", respuesta)


def insertar_datos():
    response = requests.post("http://localhost:7001/student", json={"name": "Lautaro", "courses": 3})
    print("Código de estado:", response.status_code)
    print("Contenido de la respuesta:", response.json())


def poblar_lista():
    alumnos = (
        ("Juan", 1),
        ("Sofia", 5),
        ("Martin", 2)
    )

    for nombre, cursos in alumnos:
        response = requests.post("http://localhost:7001/student", json={"name": nombre, "courses": cursos})
        print("Código de estado:", response.status_code)
        print("Contenido de la respuesta:", response.json())


def recorrer_lista():
    response = requests.get("http://localhost:7001/student")
    if response.status_code == 200:
        respuesta = response.json()
        for alumno in respuesta["students"]:
            print("---------")
            print("ID:", alumno["id"])
            print("Nombre:", alumno["name"])
            print("Cursos:", alumno["courses"])
            print("---------")
    else:
        print("Ocurrio un error")


def info_estudiante(id, formato=""):
    response = requests.get("http://localhost:7001/student/" + str(id))
    print("Código de estado:", response.status_code)
    alumno = response.json()
    print("Contenido de la respuesta:", alumno)
    if formato == "y":
        print("---------")
        print("Nombre:", alumno["name"])
        print("Cursos:", alumno["courses"])
        print("---------")


def modificar_estudiante(id, diccionario):
    response = requests.put("http://localhost:7001/student/" + str(id), json=diccionario)
    print("Código de estado:", response.status_code)
    

def eliminar_estudiante(id):
    response = requests.delete("http://localhost:7001/student/" + str(id))
    print("Código de estado:", response.status_code)


#poblar_lista()
#obtener_datos()
#insertar_datos()
#recorrer_lista()
#info_estudiante(6, formato="y")
#modificar_estudiante(6, {"name": "Lucia", "courses": 8})
#eliminar_estudiante(1)