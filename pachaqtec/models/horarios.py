from django.db import models
from .cursos import Cursos

class Horarios(models.Model):
    id = models.AutoField(primary_key=True)
    frecuencia = models.CharField(max_length=50, blank=False, null=False)
    horario = models.CharField(max_length=50, blank=False, null=False)
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.frecuencia

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        app_label = 'pachaqtec'