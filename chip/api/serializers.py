from dataclasses import fields
from rest_framework import serializers
from chip import models

class ChipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chip
        fields = '__all__'