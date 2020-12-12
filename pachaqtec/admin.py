from django.contrib import admin
from .models import Categoria, Cursos, Alumno, Cupon

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Cursos)
admin.site.register(Alumno)
admin.site.register(Cupon)