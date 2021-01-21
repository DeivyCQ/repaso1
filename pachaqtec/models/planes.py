from django.db import models
from .cursos import Cursos

class Planes(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    fecha_fin = models.DateField(default='9999-12-31')
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        app_label = 'pachaqtec'
