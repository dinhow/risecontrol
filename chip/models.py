from uuid import uuid4
from django.db import models

class Chip(models.Model):
    chip_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    chip_iccid = models.CharField(max_length=200, default='')
    chip_line_number = models.CharField(max_length=50, default='', blank=True, null=True)
    chip_plan = models.CharField(max_length=50, default='', blank=True, null=True)
    chip_company = models.CharField(max_length=50, default='', blank=True, null=True)
    chip_apn = models.CharField(max_length=50, default='', blank=True, null=True)
    chip_status = models.IntegerField(default=1)
    add_at = models.DateTimeField(auto_now_add=True, blank=True)
    add_by = models.CharField(max_length=50, default='', blank=True)
    linked_at = models.CharField(max_length=50,default='',blank=True, null=True)
    linked_by = models.CharField(max_length=50, default='', blank=True, null=True)
    #linked_in = models.CharField(max_length=50, default='', blank=True)
    cancelled_by = models.CharField(max_length=50, default='', blank=True, null=True)
    cancelled_at = models.CharField(max_length=50,default='',blank=True, null=True)
    chip_with = models.CharField(max_length=200, default='', blank=True, null=True)
    chip_with_at = models.CharField(max_length=50, default='',blank=True, null=True)
    cr_gps = models.CharField(max_length=50, default='', blank=True, null=True)
    cod_cliente = models.CharField(max_length=50, default='', blank=True, null=True)
    amount_nf = models.DecimalField(max_digits=50, default=0, blank=True, decimal_places=2, null=True)
    amount_charged = models.DecimalField(max_digits=50, default=0, blank=True, decimal_places=2, null=True)