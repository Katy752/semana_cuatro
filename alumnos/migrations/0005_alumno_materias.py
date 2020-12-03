# Generated by Django 2.2.14 on 2020-12-01 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0003_remove_materia_alumnos'),
        ('alumnos', '0004_remove_alumno_materias'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='materias',
            field=models.ManyToManyField(related_name='alumnos', to='materias.Materia'),
        ),
    ]