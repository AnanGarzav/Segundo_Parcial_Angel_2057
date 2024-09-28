from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required, permission_required

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
