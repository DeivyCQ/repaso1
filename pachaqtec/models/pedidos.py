from django.db import models
from .cursos import Cursos
from .postulantes import Postulantes

class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    importe = models.DecimalField(max_digits=6, decimal_places=2)
    moneda = models.CharField(max_length=3, blank=False, null=False)
    postulante = models.ForeignKey(Postulantes, on_delete=models.CASCADE)

    def __str__(self):
        return {
            "Postulante" : self.postulante,
            "Curso" : self.curso
        }

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        app_label = 'pachaqtec'

    