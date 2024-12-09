from django.urls import path
from .views import lista_productos, agregar_producto, editar_producto, eliminar_producto

urlpatterns = [
    path('', lista_productos, name='productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
]


