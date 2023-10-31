from django.db import models

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
