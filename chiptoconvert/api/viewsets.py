from rest_framework import viewsets
from chiptoconvert import models
from chiptoconvert.api import serializers
from rest_framework.permissions import IsAuthenticated

class ChipToConvertViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ChipToConvertSerializer
    queryset = models.ChipToConvert.objects.all()