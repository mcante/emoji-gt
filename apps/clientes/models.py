# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Mis importaciones
from decimal import Decimal
from django.utils import timezone #Agregada por mi para el manejo de la fecha

# Create your models here.


class Cliente(models.Model):
	"""
	Descripcion: Clientes del EmojiGT
	"""
	nombre = models.CharField(max_length=100, blank=True, null=True)
	telefono = models.CharField("teléfono", max_length=12, blank=True, null=True, unique=True)
	celular = models.CharField(max_length=12, blank=True, null=True, unique=True)
	celular_2 = models.CharField(max_length=12, blank=True, null=True, unique=True)
	facebook = models.CharField(max_length=200, blank=True, null=True)
	latitud = models.CharField(max_length=100, null = True, blank = True)
	longitud = models.CharField(max_length=100, null = True, blank = True)
	direccion = models.CharField("Dirección", max_length=250, null = True, blank = True)
	observaciones = models.TextField(null = True, blank = True)
	creado = models.DateField(auto_now_add=True)

	
	def __unicode__(self):
		return self.nombre

	def get_pedidos(self):
		return self.clienteventa.all().count()

	class meta:
		ordering = '-creado'

	def get_absolute_url(self):
		return reverse('clientes:perfil_cliente', kwargs={'pk':self.id})
