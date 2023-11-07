from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Comentario, Calificacion
from .forms import RegistrarUsuario, ComentarioForm, CalificacionForm
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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Se ha autenticado con éxito!")
            return redirect('cursos')
        else:
            messages.error(request, "Ha habido un error de autenticación. Por favor intente nuevamente.")
            return redirect('cursos')
    else:
        cursos = Curso.objects.all()
        ctx = {"cursos": cursos}
        return render(request, "myapp/cursos.html", ctx)


def curso(request, pk):
    try:
        curso = Curso.objects.get(id=pk)
        comentarios = Comentario.objects.filter(curso=curso)
        calificaciones = Calificacion.objects.filter(curso=curso)
        comentario_form = ComentarioForm()
        calificacion_form = CalificacionForm()
    except Curso.DoesNotExist:
        raise Http404    
    ctx = {
        "curso": curso,
        "comentarios": comentarios,
        "calificaciones": calificaciones,
        "comentario_form": comentario_form,
        "calificacion_form": calificacion_form
        }
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
    messages.success(request, "El curso fue eliminado con éxito!")
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
        

def logout_user(request):
    logout(request)
    messages.success(request, "Ha salido del sistema satisfactoriamente!")
    return redirect('cursos')


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"La cuenta {user} se ha registrado exitosamente!")
            return redirect('cursos')
    else:
        form = RegistrarUsuario()
        return render(request, 'myapp/registrar.html', {'form': form})

    return render(request, 'myapp/registrar.html', {'form': form})


def agregar_comentario(request, pk):
    curso = get_object_or_404(Curso, id=pk)
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.curso = curso
            comentario.usuario = request.user
            comentario.save()
    return redirect('curso', pk=pk)


def agregar_calificacion(request, pk):
    curso = get_object_or_404(Curso, id=pk)
    if request.method == 'POST':
        calificacion_form = CalificacionForm(request.POST)
        if calificacion_form.is_valid():
            calificacion = calificacion_form.save(commit=False)
            calificacion.curso = curso
            calificacion.usuario = request.user
            calificacion.save()
        else:
            messages.warning(request, "La calificación no es válida. Debe ser entre 0 y 5 puntos")
    return redirect('curso', pk=pk)
