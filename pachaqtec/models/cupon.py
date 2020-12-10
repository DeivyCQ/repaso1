from django.db import models

# Clase Cupon
class Cupon(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_cupon = models.CharField(max_length=30, blank=False, null=False)
    importe_cupon = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    porcentaje_cupon = models.PositiveSmallIntegerField()
    fecha_fin = models.DateField(blank=False, null=False)
    en_uso = models.BooleanField(default=False)
    por_categoria = models.BooleanField(default=False)
    por_curso = models.BooleanField(default=False)

    def __str__(self):
        return self.codigo_cupon

    class Meta:
        verbose_name = 'Cupón'
        verbose_name_plural = 'Cupones'
        app_label = 'pachaqtec'
