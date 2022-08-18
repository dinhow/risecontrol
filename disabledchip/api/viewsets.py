from rest_framework import viewsets
from chip import models
from chip.api import serializers
from rest_framework.permissions import IsAuthenticated

class ChipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ChipSerializer
    queryset = models.Chip.objects.all()