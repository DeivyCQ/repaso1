from django.db import models
from .cursos import Cursos

class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=8, null=False, blank=False)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    correo = models.EmailField(max_length=240, null=False, blank=False)
    celular = models.CharField(max_length=13, null=False, blank=False)
    cursos = models.ManyToManyField(Cursos, db_table='pachaqtec_matricula')

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        app_label = 'pachaqtec'