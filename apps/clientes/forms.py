from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'creado': forms.HiddenInput(),
        }
