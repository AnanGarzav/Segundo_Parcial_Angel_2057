# segundo_parcial/admin.py
from django.contrib import admin
from .models import Profesor, Mascota

# Registrar los modelos
admin.site.register(Profesor)
admin.site.register(Mascota)
# segundo_parcial/admin.py

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    search_fields = ['nombres', 'apellido']  # Permite buscar por nombres o apellidos
    list_filter = ['genero']  # Filtrar por género
    list_display = ['cedula', 'nombres', 'apellido', 'genero']  # Mostrar estas columnas en la lista

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'raza']  # Búsqueda por nombre o raza
    list_filter = ['genero']  # Filtrar por género
    list_display = ['id_mascota', 'nombre', 'raza', 'genero', 'cedula']  # Columnas a mostrar en la lista
