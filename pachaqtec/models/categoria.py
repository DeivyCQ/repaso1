from django.db import models

# modelo categoria
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'categorías'
        app_label = 'pachaqtec'