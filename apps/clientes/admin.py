# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Cliente


class ModelClientes(admin.ModelAdmin):
	list_display = ['nombre', 'telefono', 'celular', 'facebook', 'creado'] #Campos a mostrar
	# list_filter = ['nombre', 'telefono', 'celular', 'facebook'] #Filtros posibles para la lista
	# list_editable = ['nombre', 'telefono', 'celular', 'facebook'] #Campo que se puede editar
	search_fields = ['nombre', 'telefono', 'celular', 'facebook', 'creado'] #Posibilidad de hacer busquedar por los campos incluidos.


admin.site.register(Cliente, ModelClientes) #Se registran los modelos en el admin