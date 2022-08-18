from rest_framework import viewsets
from disabledchip import models
from disabledchip.api import serializers
from rest_framework.permissions import IsAuthenticated

class DisabledChipViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.ChipSerializer
    queryset = models.DisabledChip.objects.all()