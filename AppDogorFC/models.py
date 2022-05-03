from tabnanny import verbose
from django.db import models

# Create your models here.

class juntadirectiva(models.Model):
    nombreapellido = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.nombreapellido, self.puesto)

    class Meta:
        verbose_name = "Junta Directiva"


class jugadores(models.Model):
    nombreapellido = models.CharField(max_length=40)
    posicion = models.CharField(max_length=40)
    dorsalcamiseta = models.IntegerField()
 
    class Meta:
        verbose_name= "Jugadores"

class cuerpotecnico(models.Model):
    nombreapellido = models.CharField(max_length=40)
    funcion = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Cuerpo Tecnico"