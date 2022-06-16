from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    user_key = models.CharField(max_length=255)
    adress = models.TextField()
    contact = models.TextField()


class Cuota(models.Model):
    name = models.CharField(max_length=255)
    date_create = models.DateField(auto_now_add=True)
    date_pago = models.DateField(blank=True, null=True)
    precio = models.TextField(blank=True, null=True)


class Pago(models.Model):
    couta_pagar = models.ForeignKey(Cuota, on_delete=models.CASCADE)
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)



class Alumno(models.Model):
    curp = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    grado = models.CharField(max_length=100)
    date_create = models.DateField(auto_now_add=True)
    datos_inscripcion = models.TextField(blank=True, null=True)
