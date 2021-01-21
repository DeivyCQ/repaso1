from django.db import models
from .cursos import Cursos

class Alumnos(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    correo = models.EmailField(max_length=80)
    telefono = models.CharField(max_length=20)
    cursos = models.ManyToManyField(Cursos, blank=True, db_table='pachaqtec_matricula')

    def __str__(self):
        return self.nombres

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        app_label = 'pachaqtec'