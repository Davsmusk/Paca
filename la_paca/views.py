from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from ventas.models import Venta
from empleados.models import Empleado
from django.db.models import Sum
from clientes.models import Cliente

from productos.models import Producto

def index_view(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('logout_success')

def logout_success(request):
    return render(request, 'logout_success.html')


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

def logout_success(request): return render(request, 'logout_success.html')

