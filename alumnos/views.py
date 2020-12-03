from django.shortcuts import render
import materias
from alumnos.models import Alumno


def get_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos/lista.html', {'alumnos': alumnos})


def get_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    return render(request, 'alumnos/detalle.html', {'alumno': alumno, 'materias': materias})

