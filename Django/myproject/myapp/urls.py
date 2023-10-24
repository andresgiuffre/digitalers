from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="myindex"),
    path("acerca-de", views.acerca_de, name="acerca_de"),
    path("cursos", views.cursos, name="cursos"),
    path("curso/<str:nombre_curso>", views.curso, name="curso"),
    path("cursos/json", views.cursos_json, name="cursos_json"),
    path("aeropuertos", views.aeropuertos, name="aeropuertos"),
]