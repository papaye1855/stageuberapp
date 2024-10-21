from django.shortcuts import render , redirect
from django.http.request import HttpRequest
from django.contrib import messages
from utilisateur.models import Utilisateur
from dashboard.models import Chauffeur, Passager

# Create your views here.


def chauffeur(request:HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            user : Utilisateur = request.user
            if user.type_utilisateur == "chauffeur":
                try:
                    compteChauffeur : Chauffeur = user.chauffeur
                    return render(request, "dashboard/chauffeur.html", {"chauffeur": compteChauffeur})
                except:
                    return redirect("index")
            else:
                return redirect("index")
        else:
            messages.warning(request, "Veuillez d'abord vous connecter")
            return redirect("connexion")
    else:
        return redirect("index")


def passager(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user : Utilisateur = request.user
            if user.type_utilisateur == "passager":
                try:
                    comptePassager : Passager = user.passager
                    return render(request, "dashboard/passager.html", {"passager": comptePassager})
                except:
                    return redirect("index")
            else:
                return redirect("index")
        else:
            messages.warning(request, "Veuillez d'abord vous connecter")
            return redirect("connexion")
    else:
        return redirect("index")
