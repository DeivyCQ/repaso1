from django.db import models
from .categoria import Categoria
from .cupon import Cupon

class Cursos(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=False, blank=False)
    subtitulo = models.TextField()
    resumen = models.TextField()
    dirigido_a = models.TextField(null=True, blank=True)
    otorga = models.TextField()
    fecha_inicio = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    cupon = models.ManyToManyField(Cupon, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        app_label = 'pachaqtec'