# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from .forms import PedidoForm, DetallePedidoForm
from .models import Pedido, DetallePedido


from django.views.generic import ListView, DetailView, DeleteView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

#PEDIDO

# Listar Pedido
class ListarPedido(ListView):
	model = Pedido
	template_name = 'pedidos/listar_pedidos.html'

# Crear Pedido
class CrearPedido(CreateView):
	model = Pedido
	form_class = PedidoForm
	template_name = 'pedidos/nuevo_pedido.html'

	def get_success_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.object.id})

# Actualiza Pedido
class ModificarPedido(UpdateView):
	model = Pedido
	form_class = PedidoForm
	template_name = 'pedidos/nuevo_pedido.html'
	
	def get_success_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.object.id})


# Eliminar Pedido
class EliminarPedido(DeleteView):
	model = Pedido
	template_name = 'pedidos/eliminar_pedido.html'
	success_url = reverse_lazy('pedidos:listar_pedidos')


# Listar Pedido con su Detalle
class ListarDtPedido(DetailView):
	model = Pedido
	template_name = 'pedidos/listar_pedido_detalle.html'

	def get_context_data(self, **kwargs):
		context = super(ListarDtPedido, self).get_context_data(**kwargs)
		context['detalle_form'] = DetallePedidoForm(initial={'pedido': self.object})
		return context

# Listar Pedido con su Detalle
class MapaPedido(ListView):
	model = Pedido
	template_name = 'pedidos/mapa.html'



#DETALLE PEDIDO --------------*------------------------

# Crear Detalle Pedido
class CrearDetallePedido(CreateView):
	model = DetallePedido
	form_class = DetallePedidoForm
	template_name = 'pedidos/nuevo_detalle_pedido.html'
	

# Actualiza Detalle Pedido
class ModificarDetallePedido(UpdateView):
	model = DetallePedido
	form_class = DetallePedidoForm
	template_name = 'pedidos/nuevo_detalle_pedido.html'
	
	def get_success_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.object.pedido.id})

# Eliminar Detalle Pedido
class EliminarDetallePedido(DeleteView):
	model = DetallePedido
	template_name = 'pedidos/eliminar_detalle_pedido.html'
	
	def get_success_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.object.pedido.id})


class VentasCantidades(TemplateView):
    template_name = 'pedidos/calendar.html'

    def get_context_data(self, **kwargs):
		context = super(VentasCantidades, self).get_context_data(**kwargs)
		context['pedidos'] = Pedido.objects.all()
		context['pendiente'] = Pedido.objects.filter(estado_pedido = 1).count()
		context['entregado'] = Pedido.objects.filter(estado_pedido = 2).count()
		context['cancelado'] = Pedido.objects.filter(estado_pedido = 3).count()

		return context