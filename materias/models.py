from django.db import models
from alumnos.models import Alumno


class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=150)

    alumnos = models.ManyToManyField(Alumno, related_name='materias')
    '''materias = models.ManyToManyField(Materia, related_name='alumnos')'''

    def __str__(self):
        return self.nombre

