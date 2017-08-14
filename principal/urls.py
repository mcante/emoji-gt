"""principal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.ventas.views import VentasCantidades

from django.contrib.auth.views import login, logout_then_login

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^clientes/', include('apps.clientes.urls', namespace="clientes")),
    url(r'^cojines/', include('apps.cojines.urls', namespace="cojines")),
    url(r'^pedidos/', include('apps.ventas.urls', namespace="pedidos")),

    #CALENDARIO
    url(r'^$', login_required(VentasCantidades.as_view()), name='calendario'),


    #URL para el login  -- Si se intenta ingresar a una url que necesite autenticacion, se redireccionara a accounts/login/login para que inicie sesion
    url(r'^accounts/login/', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout', logout_then_login, name = 'cerrar_sesion'),

]
