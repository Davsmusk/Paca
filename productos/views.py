from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from ventas.models import Venta, Carrito, CarritoItem  # Corregir las importaciones
from .forms import ProductoForm
from django.contrib import messages

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos})

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('productos')
        else:
            messages.error(request, 'No se pudo agregar el producto. Por favor, complete todos los campos requeridos.')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('productos')
        else:
            messages.error(request, 'No se pudo actualizar el producto. Por favor, complete todos los campos requeridos.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})
