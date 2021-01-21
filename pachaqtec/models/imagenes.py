from django.db import models
from .cursos import Cursos

class Imagenes(models.Model):
    IMG_MAIN = '1'
    IMG_SLIDE = '2'
    IMG_TYPE = [
        (IMG_MAIN, 'Principal'), 
        (IMG_SLIDE, 'Slide'),
    ]


    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=100, blank=False, null=False)
    ruta = models.CharField(max_length=100, blank=False, null=False)
    tipo_imagen = models.CharField(max_length=1, blank=False, null=False, choices=IMG_TYPE, default=IMG_MAIN)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'