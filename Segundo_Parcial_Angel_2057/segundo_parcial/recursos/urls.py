from django.urls import path, include
from .views import (
    lista_productos,
    crear_producto,
    modificar_producto,
    eliminar_producto,
    ProfesorViewSet,
    MascotaViewSet,
    ListaMascotas,
    CrearMascota,
    ModificarMascota,
    ListaProfesores,
    CrearProfesor,
    ModificarProfesor,
)

from rest_framework.routers import DefaultRouter

# Configurar el router para la API REST
router = DefaultRouter()
router.register(r'profesores', ProfesorViewSet, basename='profesor')
router.register(r'mascotas', MascotaViewSet, basename='mascota')

# Unir todas las URLs en una sola lista
urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('modificar/<int:pk>/', modificar_producto, name='modificar_producto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('mascotas/', ListaMascotas.as_view(), name='lista_mascotas'),
    path('mascotas/<int:pk>/', ModificarMascota.as_view(), name='modificar_mascota'),
    path('profesores/', ListaProfesores.as_view(), name='lista_profesores'),
    path('profesores/<int:pk>/', ModificarProfesor.as_view(), name='modificar_profesor'),
    path('', include(router.urls)),  # Incluir las URLs del router
]
