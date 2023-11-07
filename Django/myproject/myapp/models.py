from django.db import models
from django.contrib.auth.models import User


class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    monotributista = models.BooleanField()

# Create your models here.
class Curso(models.Model):
    TURNOS = (
            ("Mañana", "Mañana"),
            ("Tarde", "Tarde"),
            ("Noche", "Noche")
        )
    nombre = models.CharField(max_length=128)
    inscripciones = models.IntegerField()
    turno = models.CharField(max_length=128, choices=TURNOS, default=1)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name="cursos")


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)


class Calificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
