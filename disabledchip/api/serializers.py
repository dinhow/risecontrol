from dataclasses import fields
from rest_framework import serializers
from disabledchip import models

class DisabledChipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DisabledChip
        fields = '__all__'