from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="myindex"),
    path("acerca-de", views.acerca_de, name="acerca_de"),
    path("cursos", views.cursos, name="cursos"),
    path("curso/<int:pk>", views.curso, name="curso"),
    path("curso/<int:pk>/agregar_comentario/", views.agregar_comentario, name="agregar_comentario"),
    path("curso/<int:pk>/agregar_calificacion/", views.agregar_calificacion, name="agregar_calificacion"),
    path("cursos/json", views.cursos_json, name="cursos_json"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
    path("nuevo-curso", views.nuevo_curso, name="nuevo_curso"),
    path("actualizar-curso/<int:pk>", views.actualizar_curso, name="actualizar_curso"),
    path("eliminar-curso/<int:pk>", views.eliminar_curso, name="eliminar_curso"),
    path("nueva-pelicula", views.nueva_pelicula, name="nueva_pelicula"),
    path("tabla-peliculas", views.tabla_peliculas, name="tabla_peliculas"),
    path("logout", views.logout_user, name="logout"),
    path("registrar", views.registrar_usuario, name="registrar"),
]