from rest_framework import viewsets
from user import models
from user.api import serializers
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()