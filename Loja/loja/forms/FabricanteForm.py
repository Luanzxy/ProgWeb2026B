from django.forms import ModelForm
from django import forms
from loja.models.Fabricante import Fabricante

class FabricanteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FabricanteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Fabricante
        fields = ['Fabricante'] 
        
        widgets = {
            'Fabricante': forms.TextInput(attrs={'class': "form-control"}),
        }