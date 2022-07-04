from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    name = models.CharField(default="CENDI J.PIAGET", max_length=250)
    inicio_curso = models.DateField()
    fin_curso = models.DateField()


class Week(models.Model):
    week = models.IntegerField()
    inicio = models.DateField()
    fin = models.DateField()
    status = models.BooleanField(default=True)


class Cuota(models.Model):
    week = models.ForeignKey(Week, on_delete=None, blank=True, null=True)
    name = models.CharField(max_length=255)
    monto = models.FloatField(blank=True, null=True)
    pronto_pago = models.FloatField(default=True, null=True)
    recargo = models.FloatField(blank=True, null=True)
    aplica = models.CharField(max_length=500)
    obligatorio = models.BooleanField(default=True)

class Alumno(models.Model):
    curp = models.CharField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    grado = models.CharField(max_length=100)
    date_create = models.DateField(blank=True, null=True)
    date_birth = models.DateField()
    datos_inscripcion = models.TextField(blank=True, null=True)


class Pago(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=CASCADE)
    cuota = models.ForeignKey(Cuota, on_delete=CASCADE)
    date_pay = models.DateTimeField(auto_now_add=True)
