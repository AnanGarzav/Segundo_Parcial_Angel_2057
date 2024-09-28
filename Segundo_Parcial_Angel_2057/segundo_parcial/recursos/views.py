from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required
from .serializers import ProfesorSerializer, MascotaSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, filters
from .models import Profesor, Mascota
from rest_framework import generics

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'recursos/lista_productos.html', {'productos': productos})

@login_required
@permission_required('recursos.add_producto', raise_exception=True)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'recursos/crear_producto.html', {'form': form})

@login_required
@permission_required('recursos.change_producto', raise_exception=True)
def modificar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'recursos/modificar_producto.html', {'form': form})

@login_required
@permission_required('recursos.delete_producto', raise_exception=True)
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'recursos/eliminar_producto.html', {'producto': producto})

# Configurar la paginación
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Número de resultados por página
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombres', 'apellido', 'genero']

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'raza', 'genero', 'cedula']

class ListaMascotas(generics.ListCreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class ModificarMascota(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class ListaProfesores(generics.ListCreateAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class ModificarProfesor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CrearMascota(generics.CreateAPIView):  
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class CrearProfesor(generics.CreateAPIView):  
    queryset = Profesor.objects.all()  # Corregido a Profesor
    serializer_class = ProfesorSerializer
