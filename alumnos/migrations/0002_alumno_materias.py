# Generated by Django 2.2.14 on 2020-12-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='materias',
            field=models.ManyToManyField(related_name='alumnos', to='materias.Materia'),
        ),
    ]
