from django.contrib import admin
from .models import Categoria, Cupon, Cursos, Planes

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Cupon)
admin.site.register(Cursos)
admin.site.register(Planes)