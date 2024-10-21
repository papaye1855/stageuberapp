from django.http.response import HttpResponse
from django.shortcuts import render
from dashboard.forms import PassagerForm , ChauffeurForm, ConnexionForm
from dashboard.models import Chauffeur
from django.views.decorators.csrf import csrf_exempt

import pusher

pusher_client = pusher.Pusher(
  app_id='REMPLACER_ICI',
  key='REMPLACER_ICI',
  secret='REMPLACER_ICI',
  cluster='REMPLACER_ICI',
)

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def mapresentation(request):
    return render(request, "informations.html")

def apropos(request):
    return render(request,"about.html")

def services(request):
    return render(request, "nos-services.html")