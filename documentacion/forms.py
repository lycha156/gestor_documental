from django import forms
from django.forms import CharField, ClearableFileInput, FileField 
from .models import Documento, Estado, Grupo
from dependencias.models import TipoDependencia, Dependencia

class Estado(forms.ModelForm):
    class meta:
        model = Estado
        fields = ['estado']

    estado = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))

class Grupo(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['grupo']

    grupo = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))

class Documento(forms.ModelForm):
    class Meta:
        model = Documento
        fields = [
            'estado',
            'fecha',
            'codigo',
            'grupo',
            'descripcion',
            'iniciador',
            'destino',
            'observaciones',
            'tags',
            'documento'
        ]

    estado = forms.ModelChoiceField(Estado.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-estado'}))
    fecha = forms.CharField(widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control', 'type': 'date'}))
    codigo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    grupo = forms.ModelChoiceField(Grupo.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-grupo'}))
    descripcion = forms.TextInput(Widget=forms.Textarea(attrs={'class': 'form-control'}))
    iniciador = forms.ModelChoiceField(Dependencia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-iniciador'}))
    destino = forms.ModelChoiceField(Dependencia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-destino'}))
    observaciones = forms.TextInput(Widget=forms.Textarea(attrs={'class': 'form-control'}))
    tags = forms.TextInput(Widget=forms.Textarea(attrs={'class': 'form-control'}))
    documento = FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))