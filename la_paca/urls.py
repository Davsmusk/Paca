"""
URL configuration for la_paca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import login_view, index_view, admin_dashboard, logout_success
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView




from django.contrib import admin
from django.urls import path, include
from .views import login_view, logout_view, index_view, admin_dashboard, logout_success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # URL para logout
    path('logout_success/', logout_success, name='logout_success'),  # URL para la página de cierre de sesión
    path('', index_view, name='index'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('productos/', include('productos.urls')),
    path('clientes/', include('clientes.urls')),
    path('ventas/', include('ventas.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
