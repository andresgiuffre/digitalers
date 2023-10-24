from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
import sqlite3


def index(request):
    ctx = {"nombre": "Juan",
           "cursos": 5,
           "curso_actual": {"nombre": "Python y Django", "turno": "noche"},
           "cursos_anteriores": ["Java", "PHP", "JavaScript", "Python"]
           }
    return render(request, "myapp/index.html", ctx)


def acerca_de(request):
    return HttpResponse("Este es el curso de Python y Django!!")


def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos")
    cursos = cursor.fetchall()
    conn.close()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)


def curso(request, nombre_curso):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos WHERE nombre=?", [nombre_curso])
    curso = cursor.fetchone()
    
    if curso is None:
        raise Http404
    
    ctx = {"curso": curso}
    conn.close()
    return render(request, "myapp/curso.html", ctx)


def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response


def aeropuertos(request):
    archivo = open("aeropuertos.csv", encoding="utf8")
    lista_aeropuertos = []
    for linea in archivo:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        lista_aeropuertos.append((nombre, ciudad, pais))
    archivo.close()
    ctx = {"lista_aeropuertos": lista_aeropuertos}
    return render(request, "myapp/aeropuertos.html", ctx)