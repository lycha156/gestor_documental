from django.db import models

class Historial(models.Model):

    class Meta:
        verbose_name_plural = "Historiales"

    ACCION_CHOICES = [
        ('A', 'ALTA'),
        ('B', 'BAJA'),
        ('M', 'MODIFICACION')
    ]
    
    fecha = models.DateTimeField(("Fecha y Hora"), auto_now_add=True)
    usuario = models.CharField(("usuario"), max_length=50)
    accion = models.CharField(("Accion"), max_length=50, choices=ACCION_CHOICES)
    tabla = models.CharField(("Tabla"), max_length=50)
    descripcion = models.TextField(("Descripcion"))
    

    def __str__(self):
        return f'{self.fecha.strftime("%Y-%m-%d %H:%M:%S")} (UID:{self.usuario}) - (ACCION: {self.get_accion_display()}) - (TABLA: {self.tabla})'
    