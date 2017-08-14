from django import forms
from django.forms import ModelForm
from .models import Material, Cojin

class MaterialesForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            'modificado': forms.HiddenInput(),
        }


class CojinForm(forms.ModelForm):
    class Meta:
        model = Cojin
        fields = '__all__'
        widgets = {
            'creado': forms.HiddenInput(),
        }
