from django.db import models

# Create your models here.
class Parcelas(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    poligono = models.IntegerField()
    parcela = models.IntegerField()

    def __unicode__(self):
        return self.parcela

    class Meta:
        verbose_name_plural = "Parcelas"