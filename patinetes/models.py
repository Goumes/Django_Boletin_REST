from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Patinete(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50)
    precio_desbloqueo = models.DecimalField(decimal_places=2, max_digits=5)
    precio_minuto = models.DecimalField(decimal_places=2, max_digits=5)


class Usuario(models.Model):
    debito = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)


class Alquiler(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    patinete = models.ForeignKey(
        Patinete,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    fecha_desbloqueo = models.DateField()
    fecha_entrega = models.DateField()
    coste_final = models.DecimalField(decimal_places=2, max_digits=5)
