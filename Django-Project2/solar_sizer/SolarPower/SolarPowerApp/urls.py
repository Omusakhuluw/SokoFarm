from django.urls import path
from . import views

urlpatterns = [
    path("", views.SolarPowerApp, name="SolarPowerApp"),
]