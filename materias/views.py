from django.shortcuts import render
from materias.models import Materia


def get_materias(request):
    materias = Materia.objects.all()
    return render(request, 'materias/Listas.html', {'materias': materias})


def get_materia(request, materia_id):
    materia = Materia.objects.get(id=materia_id)
    alumnos = materia.alumnos.all()
    return render(request, 'materias/detalles.html', {'materias': materia, 'alumnos': alumnos})




