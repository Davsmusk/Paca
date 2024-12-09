from django.urls import path
from .views import clientes_view, agregar_cliente, editar_cliente, eliminar_cliente

urlpatterns = [
    path('', clientes_view, name='clientes'),
    path('agregar/', agregar_cliente, name='agregar_cliente'),
    path('editar/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('eliminar/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
]
