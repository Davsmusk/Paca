from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Empleado
from .forms import EmpleadoForm
from productos.models import Producto
from ventas.models import Venta
from empleados.models import Empleado 
from clientes.models import Cliente
from django.db.models import Sum

@login_required
def empleados_view(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})

@login_required
def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})

@login_required
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/editar_empleado.html', {'form': form})

@login_required
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleados')
    return render(request, 'empleados/eliminar_empleado.html', {'empleado': empleado})




@login_required
def admin_dashboard(request):
    total_ventas = Venta.objects.count()
    ventas_totales = Venta.objects.aggregate(total=Sum('cantidad'))['total'] or 0

    productos = Producto.objects.all()
    empleados = Empleado.objects.all()

    ventas_por_cliente = Cliente.objects.annotate(total_compras=Sum('venta__cantidad'))
    ventas_por_producto = Producto.objects.annotate(total_vendido=Sum('venta__cantidad'))

    context = {
        'total_ventas': total_ventas,
        'ventas_totales': ventas_totales,
        'productos': productos,
        'empleados': empleados,
        'ventas_por_cliente': ventas_por_cliente,
        'ventas_por_producto': ventas_por_producto,
    }
    return render(request, 'admin_dashboard.html', context)

