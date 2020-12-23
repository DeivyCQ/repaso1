from django.db import models
from .planes import Planes

class Unidades(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20, blank=False, null=False)
    planes = models.ForeignKey(Planes, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        app_label = 'pachaqtec'