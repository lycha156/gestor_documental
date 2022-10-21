from django.db import models

class TipoDependencia(models.Model):
    tipo = models.CharField("Tipo", max_length = 50)

    def __str__(self):
        return self.tipo
    

class Dependencia(models.Model):
    nombre = models.CharField("nombre", max_length = 100)
    direccion = models.CharField("Direccion", max_length=100)
    telefono = models.CharField("Telefono", max_length=50)
    interno = models.IntegerField("Interno")
    email = models.EmailField("Email", max_length=254)
    encargado = models.CharField("Encargado", max_length=50)
    observaciones = models.TextField("Observaciones")
    tipo = models.ForeignKey(TipoDependencia, related_name="tipo_dependencia", on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre
    