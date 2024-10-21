
from django.contrib import admin
from django.urls import path, include
from .views import *


app_name = "AuthGateway"
urlpatterns = [
    path("valider_inscription_passager/", valider_inscription_passager, name="valider_inscription_passager"),
    path("valider_inscription_chauffeur/", valider_inscription_chauffeur, name="valider_inscription_chauffeur"),
    path("valider_connexion/", valider_connexion, name="valider_connexion"),
    path("deconnexion/", deconnexion, name="deconnexion")
]
