from django.urls import path
from . import views

urlpatterns=[
    path=('SolarPowerApp/', views.SolarPowerApp, name='SolarPowerApp'),
]