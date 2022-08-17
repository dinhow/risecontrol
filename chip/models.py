from uuid import uuid4
from django.db import models

class Chips(models.Model):
    chip_id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    chip_iccid = models.CharField(max_length=22, unique=True, default='')
    chip_company = models.CharField(max_length=20, default='')
    chip_apn = models.CharField(max_length=20, default='')
    chip_status = models.IntegerField(default=1)
    add_at = models.DateTimeField(auto_now_add=True)
    linked_at = models.DateTimeField(auto_now=True)
    linked_by = models.CharField(max_length=50, default='')
    linked_in = models.CharField(max_length=50, default='', unique=True)
    cancelled_by = models.CharField(max_length=50, default='')
    cancelled_at = models.DateTimeField(auto_now=True)
    chip_with = models.CharField(max_length=50, default='')
    chip_with_at = models.DateTimeField(auto_now = True)