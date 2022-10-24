from django.db import models

# SOLO POR ADMIN - NO CRUD
class TipoDependencia(models.Model):
    tipo = models.CharField("Tipo", max_length = 50)

    def __str__(self):
        return self.tipo
    

class Dependencia(models.Model):
    nombre = models.CharField("nombre", max_length = 100)
    direccion = models.CharField("Direccion", max_length=100, blank=True)
    telefono = models.CharField("Telefono", max_length=50, blank=True)
    interno = models.IntegerField("Interno", blank=True)
    email = models.EmailField("Email", max_length=254, blank=True)
    encargado = models.CharField("Encargado", max_length=50, blank=True)
    observaciones = models.TextField("Observaciones", blank=True)
    tipo = models.ForeignKey(TipoDependencia, related_name="tipo_dependencia", on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre
    