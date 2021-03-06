from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Sum

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
    activa = models.BooleanField(default=True)

    def cuotas_total(self):
        cuotas = self.cuota_set.aggregate(Sum('monto'))
        return cuotas


    def pagos_total(self):
        pagos = self.pago_set.aggregate(Sum('total_pagado'))
        if pagos['total_pagado__sum']:
            return pagos
        return {'total_pagado__sum': 0.0}


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
    cuota = models.ForeignKey(Cuota, blank=True, null=True, on_delete=CASCADE)
    producto = models.ForeignKey('Producto', blank=True, null=True, on_delete=CASCADE)
    total_pagado = models.FloatField(default=0)
    monto_original = models.FloatField(default=0)
    recargos = models.FloatField(default=0)
    week_payment = models.ForeignKey(Week, blank=True, null=True, on_delete=CASCADE)
    date_pay = models.DateTimeField(auto_now_add=True)

    
class Ticket(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=CASCADE)
    pago = models.ManyToManyField(Pago, blank=True, null=True)
    date_pago = models.DateField(auto_now_add=True)


class Producto(models.Model):
    product_name = models.CharField(max_length=500)
    sizes = models.CharField(max_length=500, default=0)
    price = models.FloatField()
    grade = models.CharField(max_length=100)

