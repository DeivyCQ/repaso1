from django.db import models
from .cupon import Cupon

# modelo categoria
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)
    cupon = models.ManyToManyField(Cupon, limit_choices_to={"por_categoria":True})

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        app_label = 'pachaqtec'