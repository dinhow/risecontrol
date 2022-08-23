from re import X
from uuid import uuid4
from django.db import models

class ChipToConvert(models.Model):
    chip_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    mb = models.CharField(max_length=22, default='--', blank=True)
    vlrnf = models.CharField(max_length=20, default='--', blank=True)
    x = models.CharField(max_length=200,default='--', blank=True)
    serial = models.CharField(max_length=50,default='--', blank=True)
    localizacao = models.CharField(max_length=200, default='--', blank=True)
    codcliente = models.CharField(max_length=50,default='--', blank=True)
    crgps = models.CharField(max_length=50,default='--', blank=True)
    vlrcobrado = models.CharField(max_length=10,default='--', blank=True)
    forn = models.CharField(max_length=50, default='--', blank=True)
    operadora = models.CharField(max_length=50, default='--', blank=True)
    termino = models.CharField(max_length=50, default='--', blank=True)
    status = models.CharField(max_length=50, default='--', blank=True)
    oservico = models.CharField(max_length=50, default='--', blank=True)
    checklinha2148 = models.CharField(max_length=50, default='--', blank=True)