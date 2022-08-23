from dataclasses import fields
from rest_framework import serializers
from chiptoconvert import models

class ChipToConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChipToConvert
        fields = '__all__'