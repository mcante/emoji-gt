# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Mis importaciones
from decimal import Decimal
from django.utils import timezone #Agregada por mi para el manejo de la fecha

# Create your models here.


class Material(models.Model):
	nombre = models.CharField(max_length=100, blank=True, null=True)
	descripcion = models.CharField("descripción", max_length=100, blank=True, null=True)
	precio_yarda = models.DecimalField("precio por yarda", max_digits=6, decimal_places=2, null = True, blank = True)
	modificado = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.nombre

	class meta:
		ordering = 'nombre'


class Cojin(models.Model):
	nombre = models.CharField(max_length=150, blank=True, null=True)
	tamanio = models.IntegerField("tamaño", default=0)
	material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='materiales')
	costo = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
	precio = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True, default=Decimal('0.00'))
	creado = models.DateField(auto_now_add=True)
	
	def __unicode__(self):
		return '{} {} {} {} {} {} {}'.format('Q.', self.precio, ' - ', self.nombre, self.tamanio, " cm", self.material)

	class meta:
		ordering = '-nombre'
