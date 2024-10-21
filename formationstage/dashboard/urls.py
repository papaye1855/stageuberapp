
from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "Dashboard"
urlpatterns = [
    path("chauffeur/", chauffeur, name="chauffeur"),
    path("passager/", passager, name="passager")
]
