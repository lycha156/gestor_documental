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
    
    # DESCRIPCION CORTA PARA USAR EN HISTORIAL
    @property
    def descripcion_corta(self):
        return f'(ID:{self.id}) D: {self.descripcion} (UID: {self.usuario}, Fecha: {self.fecha}, Codigo: {self.codigo}, Grupo: {self.grupo}, I: {self.iniciador} ==> D: {self.destino} Documento: {self.documento})'

    # DESCRIPCION COMPLETA DEL DOCUMENTO
    @property
    def historial(self):
        return f'Usuario: {self.usuario}, Estado: {self.estado}, Fecha: {self.fecha}, Codigo: {self.codigo}, Grupo: {self.grupo}, Descripcion: {self.descripcion}, Iniciador: {self.iniciador}: Destino: {self.destino}, Observaciones: {self.observaciones}, TAGS: {self.tags}'
    
class DocumentoRelacion(models.Model):
    documento = models.ForeignKey(Documento, on_delete=models.RESTRICT, related_name="documento_relacion")
    padre = models.ForeignKey(Documento, on_delete=models.RESTRICT, related_name="padre_relacion")

    def __str__(self):
        return f"{self.documento} => {self.padre}"