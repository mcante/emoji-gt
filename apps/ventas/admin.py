# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Pedido, DetallePedido, EstadoPedido

class ModelEstado(admin.ModelAdmin):
	list_display = ['estado'] #Campos a mostrar
	search_fields = ['estado'] #Posibilidad de hacer busquedar por los campos incluidos.

class ModelPedido(admin.ModelAdmin):
	list_display = ['cliente', 'estado_pedido'] #Campos a mostrar
	search_fields = ['cliente','estado_pedido'] #Posibilidad de hacer busquedar por los campos incluidos.

class ModelDetallePedido(admin.ModelAdmin):
	list_display = ['pedido', 'cojin', 'precio', 'cantidad', 'descuento', 'get_venta'] #Campos a mostrar
	search_fields = ['pedido', 'cojin', 'precio', 'cantidad', 'descuento', 'get_venta'] #Posibilidad de hacer busquedar por los campos incluidos.


admin.site.register(EstadoPedido, ModelEstado) #Se registran los modelos en el admin
admin.site.register(Pedido, ModelPedido) #Se registran los modelos en el admin
admin.site.register(DetallePedido, ModelDetallePedido) #Se registran los modelos en el admin