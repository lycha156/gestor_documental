from django import forms
from django.forms import CharField, ClearableFileInput, FileField 
from .models import Documento, Estado, Grupo
from dependencias.models import TipoDependencia, Dependencia

class EstadoForm(forms.ModelForm):
    class meta:
        model = Estado
        fields = ['estado']

    estado = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['grupo']

    grupo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}))

class DocumentoForm(forms.ModelForm):
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
    codigo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    grupo = forms.ModelChoiceField(Grupo.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-grupo'}))
    descripcion = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;', 'placeholder': 'Descripcion'}))
    iniciador = forms.ModelChoiceField(Dependencia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-iniciador'}))
    destino = forms.ModelChoiceField(Dependencia.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-select', 'id': 'select2-destino'}))
    observaciones = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;', 'placeholder': 'Observaciones'}))
    tags = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 110px;', 'placeholder': 'TAGS'}))
    documento = FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))