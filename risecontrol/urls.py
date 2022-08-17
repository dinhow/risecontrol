"""imaseg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from user import views
from user.api import viewsets as userviewsets
#from budgets.api import viewsets as budgetsviewsets
from chip.api import viewsets as chipviewsets

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

route = routers.DefaultRouter()

route.register(r'user', userviewsets.UserViewSet, basename="User")
# route.register(r'budgets', budgetsviewsets.BudgetsViewSet, basename="Budgets")
# route.register(r'schedules', budgetviewsets.BudgetsViewSet, basename="Schedules")
route.register(r'chip', chipviewsets.ChipViewSet, basename="Chip")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    #path('account/register', views.UserCreate.as_view()),
    path('', include(route.urls)),
]
