from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from dependencias.models import TipoDependencia, Dependencia
from django.core.validators import FileExtensionValidator

class Estado(models.Model):
    estado = models.CharField("Estado", max_length=50)

    def __str__(self):
        return self.estado
    

class Grupo(models.Model):
    grupo = models.CharField("Grupo", max_length = 80)

    def __str__(self):
        return self.grupo


class Documento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="usuario_documento")
    estado = models.ForeignKey(Estado, on_delete=models.RESTRICT, related_name="estado_documento")
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)
    codigo = models.CharField("Codigo", max_length= 50, blank=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.RESTRICT, related_name="grupo_documento")
    descripcion = models.TextField("Descripcion", blank=True)
    iniciador = models.ForeignKey(Dependencia, on_delete=models.RESTRICT, related_name="iniciador_documento")
    destino = models.ForeignKey(Dependencia, on_delete=models.RESTRICT, related_name="destino_documento")
    observaciones = models.TextField("Observaciones", blank=True)
    tags = models.TextField("TAGS", blank=True)
    documento = models.FileField('Documento', upload_to ="documentos/", null=False, blank=False, validators=[FileExtensionValidator(['pdf', 'jpg', 'png', 'doc', 'docx', 'xlsx'])])

    def __str__(self):
        return self.descripcion
    