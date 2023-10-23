from django.http import HttpResponse, JsonResponse
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


def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response

