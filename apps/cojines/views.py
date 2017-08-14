# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from .forms import MaterialesForm, CojinForm
from .models import Material, Cojin


from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# MATERIALES

# Listar materiales
class ListarMateriales(ListView):
	model = Material
	template_name = 'cojines/listar_materiales.html'

# Crear materiales
class CrearMateriales(CreateView):
	model = Material
	form_class = MaterialesForm
	template_name = 'cojines/crear_material.html'
	success_url = reverse_lazy('cojines:listar_materiales')

# Actualiza Material
class ModificarMaterial(UpdateView):
	model = Material
	form_class = MaterialesForm
	template_name = 'cojines/crear_material.html'
	success_url = reverse_lazy('cojines:listar_materiales')

# Eliminar Material
class EliminarMaterial(DeleteView):
	model = Material
	template_name = 'cojines/eliminar_material.html'
	success_url = reverse_lazy('cojines:listar_materiales')



# COJINES

# Listar cojines
class ListarCojines(ListView):
	model = Cojin
	template_name = 'cojines/listar_cojines.html'

# Crear materiales
class CrearCojines(CreateView):
	model = Cojin
	form_class = CojinForm
	template_name = 'cojines/crear_cojin.html'
	success_url = reverse_lazy('cojines:listar_cojines')

# Actualiza Material
class ModificarCojines(UpdateView):
	model = Cojin
	form_class = CojinForm
	template_name = 'cojines/crear_cojin.html'
	success_url = reverse_lazy('cojines:listar_cojines')

# Eliminar Material
class EliminarCojines(DeleteView):
	model = Cojin
	template_name = 'cojines/eliminar_cojin.html'
	success_url = reverse_lazy('cojines:listar_cojines')