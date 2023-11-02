from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Curso
from . import forms
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
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)


def curso(request, nombre_curso):
    try:
        curso = Curso.objects.get(nombre=nombre_curso)
    except Curso.DoesNotExist:
        raise Http404    
    ctx = {"curso": curso}
    return render(request, "myapp/curso.html", ctx)


def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response


def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:    
        form = forms.FormularioCurso()
    ctx = { "form": form }
    return render(request, "myapp/nuevo_curso.html", ctx)


def actualizar_curso(request, pk):
    curso_actual = Curso.objects.get(id=pk) #Obtengo el registro de la BBDD
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST, instance=curso_actual)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso(instance=curso_actual)
    return render(request, 'myapp/actualizar_curso.html', {'form': form})


def eliminar_curso(request, pk):
    eliminar_curso = Curso.objects.get(id=pk)
    eliminar_curso.delete()
    return HttpResponseRedirect(reverse("cursos"))


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


def nueva_pelicula(request):
    if request.method == "POST":
        form = forms.FormularioPelicula(request.POST)
        if form.is_valid():
            conn = sqlite3.connect("cursos.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO cine VALUES (?, ?, ?, ?)", (form.cleaned_data["nombre"], form.cleaned_data["fecha_estreno"], form.cleaned_data["edad_minima"], form.cleaned_data["preventa_online"]))
            conn.commit()
            conn.close()
            ctx = {"pelicula": form.cleaned_data}
            return render(request, "myapp/nueva_pelicula_creada.html", ctx)
    else:
        form = forms.FormularioPelicula()
    ctx = {"form": form}
    return render(request, "myapp/nueva_pelicula.html", ctx)


def tabla_peliculas(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, fecha_estreno, edad_minima, preventa_online FROM cine")
    peliculas = cursor.fetchall()
    conn.close()
    ctx = {"peliculas": peliculas}
    return render(request, "myapp/tabla_peliculas.html", ctx)
        