from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField(null=True)
    activo = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.nombre
