# -*- coding: utf-8 -*-

from __future__ import absolute_import

from django.db import models

# Mis importaciones
from decimal import Decimal
from django.utils import timezone #Agregada por mi para el manejo de la fecha
from apps.clientes.models import Cliente
from apps.cojines.models import Cojin
from django.core.urlresolvers import reverse_lazy, reverse

# Create your models here.
class EstadoPedido(models.Model):
	estado = models.CharField(max_length=150)

	def __unicode__(self):
		return self.estado

class Pedido(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clienteventa')
	fecha_pedido = models.DateField(default=timezone.now)
	fecha_entrega = models.DateField(default=timezone.now)
	adelanto = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
	estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, default=1)
	observaciones = models.TextField(null = True, blank = True)

	def __unicode__(self):
		return '{} {} {}'.format(self.cliente.nombre, " - fecha: ", self.fecha_pedido)

	def get_total(self):
		return sum(t.get_venta() for t in self.pedidodetalle.all())

	def get_saldo(self):
		return self.get_total() - self.adelanto

	class meta:
		ordering = '-fecha'

	def get_absolute_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.id})


class DetallePedido(models.Model):
	pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedidodetalle')
	cojin = models.ForeignKey(Cojin, on_delete=models.CASCADE, related_name='cojindetalle')
	precio = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
	cantidad = models.IntegerField(default=1)
	bordado = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
	descuento = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))

	def get_absolute_url(self):
		return reverse('pedidos:listar_pedidos_con_detalle', kwargs={'pk':self.pedido.id})

	def get_venta(self):
		return (self.precio  * self.cantidad)+ (self.bordado * self.cantidad) - self.descuento
	