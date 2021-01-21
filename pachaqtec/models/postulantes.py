from django.db import models
from .cursos import Cursos

class Postulantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80, blank=False, null=False)
    apellidos = models.CharField(max_length=80, blank=False, null=False)
    correo = models.EmailField(max_length=80)
    telefono = models.CharField(max_length=20)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}, {self.nombres}"

    class Meta:
        verbose_name = 'Postulante'
        verbose_name_plural = 'Postulantes'
        app_label = 'pachaqtec'