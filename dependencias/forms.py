from django import forms
from django import forms
from .models import TipoDependencia, Dependencia

class DependenciaForm(forms.ModelForm):
    class Meta:
        model = Dependencia
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'interno',
            'email',
            'encargado',
            'observaciones',
            'tipo'
        ]

    nombre = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control', 'autofocus': 'autofocus', 'placeholder': 'Dependencia'}))
    direccion = forms.CharField(required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Direccion'}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Telefono'}))
    interno = forms.IntegerField(required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Interno', 'type': 'numeric'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}))
    encargado = forms.CharField(required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Encargado'}))
    observaciones = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;', 'placeholder': 'Observaciones'}))
    tipo = forms.ModelChoiceField(TipoDependencia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-tipo'}))