# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from .forms import ClienteForm
from apps.ventas.forms import PedidoSubForm

from .models import Cliente
from apps.ventas.models import Pedido

from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#CLIENTE

# Listar cliente
class ListarClientes(ListView):
	model = Cliente
	template_name = 'clientes/listar.html'

# Crear cliente
class CrearCliente(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'clientes/crearcliente.html'
	
	def get_success_url(self):
		return reverse('clientes:perfil_cliente', kwargs={'pk':self.object.id})

# Actualiza Cliente
class ModificarCliente(UpdateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'clientes/crearcliente.html'
	
	def get_success_url(self):
		return reverse('clientes:perfil_cliente', kwargs={'pk':self.object.id})

# Eliminar Cliente
class EliminarCliente(DeleteView):
	model = Cliente
	template_name = 'clientes/eliminar_cliente.html'
	success_url = reverse_lazy('clientes:listar_clientes')

# Perfil del cliente con sus respectivos pedidos
class PerfilCliente(DetailView):
	model = Cliente
	template_name = 'clientes/perfil.html'

	def get_context_data(self, **kwargs):
		context = super(PerfilCliente, self).get_context_data(**kwargs)
		context['pedido_form'] = PedidoSubForm(initial={'cliente': self.object})
		context['pendiente'] = Pedido.objects.filter(estado_pedido = 1, cliente = self.object).count()
		context['entregado'] = Pedido.objects.filter(estado_pedido = 2, cliente = self.object).count()
		context['cancelado'] = Pedido.objects.filter(estado_pedido = 3, cliente = self.object).count()
		return context