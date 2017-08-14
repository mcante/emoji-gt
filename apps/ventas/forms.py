from django import forms
from django.forms import ModelForm
from .models import Pedido, DetallePedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'fecha_pedido': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'datepicker'}),
        }

class PedidoDosForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
        	'observaciones': forms.HiddenInput()
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'
        widgets = {
        	'pedido': forms.HiddenInput()
        }

class PedidoSubForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'cliente': forms.HiddenInput(),
            'fecha_pedido': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'datepicker'}),
        }