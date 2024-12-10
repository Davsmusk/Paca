from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Venta,  CarritoItem
from .forms import VentaForm
from productos.models import Producto

@login_required
def ventas_view(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/ventas.html', {'ventas': ventas})

@login_required
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form = VentaForm()
    return render(request, 'ventas/registrar_venta.html', {'form': form})

@login_required
def editar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/editar_venta.html', {'form': form})

@login_required
def eliminar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ventas')
    return render(request, 'ventas/eliminar_venta.html', {'venta': venta})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': producto.precio * cantidad
        })
        total += producto.precio * cantidad

    return render(request, 'ventas/carrito.html', {'items': items, 'total': total})


from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Venta, Cliente
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def finalizar_compra(request):
    try:
        if request.method == 'POST':
            logger.debug("Método POST recibido")
            cliente_id = request.POST.get('cliente_id')
            logger.debug(f"Cliente ID: {cliente_id}")
            cliente = Cliente.objects.get(id=cliente_id)
            total = calcular_total(request)
            logger.debug(f"Total calculado: {total}")
            venta = Venta(cliente=cliente, total=total)
            venta.save()
            logger.debug("Venta guardada correctamente")

            # Redirigir a la página de confirmación de compra
            return redirect('compra_confirmacion')
        return redirect('carrito')
    except Cliente.DoesNotExist:
        logger.error("Cliente no encontrado.")
        return render(request, 'error.html', {'mensaje': 'Cliente no encontrado. Por favor, verifique su ID de cliente.'})
    except Exception as e:
        logger.error(f"Error en finalizar_compra: {e}")
        return render(request, 'error.html', {'mensaje': 'Ocurrió un error al procesar la compra. Por favor, intente nuevamente.'})

@csrf_exempt
def finalizar_compra(request):
    try:
        if request.method == 'POST':
            print("Método POST recibido")
            cliente_id = request.POST.get('cliente_id')
            print(f"Cliente ID: {cliente_id}")
            cliente = Cliente.objects.get(id=cliente_id)
            total = calcular_total(request)
            print(f"Total calculado: {total}")
            venta = Venta(cliente=cliente, total=total)
            venta.save()
            print("Venta guardada correctamente")

            # Redirigir a la página de confirmación de compra
            return redirect('compra_confirmacion')
        return redirect('carrito')
    except Exception as e:
        # Log the error or print it to the console for debugging
        print(f"Error en finalizar_compra: {e}")
        return render(request, 'error.html', {'mensaje': 'Ocurrió un error al procesar la compra. Por favor, intente nuevamente.'})



# la_paca/views.py
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import json

@csrf_exempt
def recibir_datos_compra(request):
    if request.method == 'POST':
        datos_compra = json.loads(request.body)
        # Aquí puedes procesar los datos y guardarlos en tu dashboard
        # Por ejemplo, puedes guardar los datos en tu base de datos
        
        # Redirigir al usuario a la página de inicio
        return HttpResponseRedirect(reverse('index'))
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

# la_paca/views.py
from django.shortcuts import render

def compra_confirmacion(request):
    return render(request, 'compra_confirmacion.html')

from .models import CarritoItem

def calcular_total(request):
    carrito_items = CarritoItem.objects.all()  # Ajusta esto para filtrar por usuario o sesión si es necesario
    total = sum(item.subtotal for item in carrito_items)
    return total
