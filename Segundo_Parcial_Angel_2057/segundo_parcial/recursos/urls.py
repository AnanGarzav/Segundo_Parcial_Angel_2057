from django.urls import path
from .views import lista_productos, crear_producto, modificar_producto, eliminar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('modificar/<int:pk>/', modificar_producto, name='modificar_producto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
]
