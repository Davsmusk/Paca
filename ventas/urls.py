from django.urls import path
from .views import ventas_view, registrar_venta, editar_venta, eliminar_venta, ver_carrito, agregar_al_carrito, finalizar_compra, recibir_datos_compra, compra_confirmacion

urlpatterns = [
    path('', ventas_view, name='ventas'),
    path('registrar/', registrar_venta, name='registrar_venta'),
    path('editar/<int:pk>/', editar_venta, name='editar_venta'),
    path('eliminar/<int:pk>/', eliminar_venta, name='eliminar_venta'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('finalizar/', finalizar_compra, name='finalizar_compra'),
    path('recibir-datos-compra/', recibir_datos_compra, name='recibir_datos_compra'),
    path('compra-confirmacion/', compra_confirmacion, name='compra_confirmacion'),
]
