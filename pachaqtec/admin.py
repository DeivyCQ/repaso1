from django.contrib import admin
from .models import (
    Categoria, Cursos, Alumno, Cupon,
    Horarios, Planes, Unidades, Semanas
)

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Cursos)
admin.site.register(Alumno)
admin.site.register(Cupon)
admin.site.register(Horarios)
admin.site.register(Planes)
admin.site.register(Unidades)
admin.site.register(Semanas)