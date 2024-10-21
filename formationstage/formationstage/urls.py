"""
URL configuration for formationstage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index , name="index"),
    path("contactez-nous/", contact, name="contact"),
    path("mes-informations/", mapresentation, name="mapresentation"),
    path("apropos/",apropos, name="apropos"),
    path("services/",services, name="services"),
    path("inscription-passager/", inscription_passager, name="inscription_passager"),
    path("inscription-chauffeur/", inscription_chauffeur, name="inscription_chauffeur"),
    path("connexion/", connexion, name="connexion"),
    path("auth_gateway/", include("auth_gateway.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("avoir_chauffeur.geojson/", avoir_chauffeur ,name="avoir_chauffeur"),
    path("commander_nouvelle_course/", notifier_commande_course, name="notifier_commande_course"),
    path("course_nouveau_chat/", notifier_course_chat_message, name="notifier_course_chat_message")
]
