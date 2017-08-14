# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Material, Cojin

# Register your models here.


class ModelMaterial(admin.ModelAdmin):
	list_display = ['nombre', 'descripcion', 'precio_yarda', 'modificado'] #Campos a mostrar
	# list_filter = ['nombre', 'descripcion', 'precio_yarda']  #Filtros posibles para la lista
	# list_editable = ['nombre', 'descripcion', 'precio_yarda']  #Campo que se puede editar
	search_fields = ['nombre', 'descripcion', 'precio_yarda', 'modificado']  #Posibilidad de hacer busquedar por los campos incluidos.


class ModelCojin(admin.ModelAdmin):
	list_display = ['nombre', 'tamanio', 'material', 'costo', 'precio'] #Campos a mostrar
	# list_filter = ['nombre', 'tamanio', 'material', 'costo', 'precio']  #Filtros posibles para la lista
	# list_editable = ['nombre', 'tamanio', 'material', 'costo', 'precio']  #Campo que se puede editar
	search_fields = ['nombre', 'tamanio', 'material', 'costo', 'precio']  #Posibilidad de hacer busquedar por los campos incluidos.

admin.site.register(Material, ModelMaterial) #Se registran los modelos en el admin
admin.site.register(Cojin, ModelCojin) #Se registran los modelos en el admin