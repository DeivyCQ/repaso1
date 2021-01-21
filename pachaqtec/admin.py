from django.contrib import admin
from .models import (
    Categoria, Cupon, Cursos, Planes,
    Alumnos, Unidades, Semanas, Horarios,
    Postulantes, Imagenes, Pedidos
)


# Register your models here.
# Categoria
admin.site.register(Categoria)
# Cupón
admin.site.register(Cupon)
# Cursos
class CursosAdmin(admin.ModelAdmin):
    date_hierarchy = 'fecha_inicio'
    prepopulated_fields = {"slug" : ("titulo",)}
admin.site.register(Cursos, CursosAdmin)
# Planes
admin.site.register(Planes)
# Alumnos 
admin.site.register(Alumnos)
admin.site.register(Unidades)
admin.site.register(Semanas)
admin.site.register(Postulantes)
admin.site.register(Horarios)
admin.site.register(Imagenes)
admin.site.register(Pedidos)