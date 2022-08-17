from uuid import uuid4
from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=20, unique=True)
    userlevel = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # password = models.CharField(max_length=50)
    # set_password = models.CharField(max_length=50)