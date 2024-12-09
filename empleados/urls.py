from django.urls import path
from .views import empleados_view, agregar_empleado, editar_empleado, eliminar_empleado

urlpatterns = [
    path('', empleados_view, name='empleados'),
    path('agregar/', agregar_empleado, name='agregar_empleado'),
    path('editar/<int:pk>/', editar_empleado, name='editar_empleado'),
    path('eliminar/<int:pk>/', eliminar_empleado, name='eliminar_empleado'),
]
