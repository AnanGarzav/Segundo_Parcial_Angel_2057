from django.contrib import admin
from .models import Categoria, Producto,Profesor,Mascota

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Profesor)
admin.site.register(Mascota)