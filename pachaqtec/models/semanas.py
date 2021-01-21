from django.db import models
from .unidades import Unidades

class Semanas(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20, blank=False, null=False)
    descripcion = models.CharField(max_length=20, blank=False, null=False)
    temas = models.TextField(blank=False, null=False)
    unidades = models.ForeignKey(Unidades, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Semana'
        verbose_name_plural = 'Semanas'
        app_label = 'pachaqtec'