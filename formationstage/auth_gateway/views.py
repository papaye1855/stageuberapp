from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from dashboard.forms import PassagerForm , ChauffeurForm, ConnexionForm
from dashboard.models import Passager, Chauffeur
from utilisateur.models import Utilisateur
from django.contrib import messages

from django.contrib.auth import login , logout, authenticate

# Create your views here.

def valider_inscription_passager(request:HttpRequest):
    if request.method == "POST":
        form = PassagerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            courriel = data["courriel"]
            nom = data["nom"]
            prenom = data["prenom"]
            mdp = data["mdp"]
            taille = data["taille"]
            courriel = str(courriel).lower()

            try:
                utilisateurExiste = Utilisateur.objects.get(pseudo=courriel)
                messages.info(request, "Un compte utilisateur existe déjà avec le courriel que vous avez fourni")
                return redirect("inscription_passager")
            except:
                newUtilisateur = Utilisateur(nom=nom, prenom=prenom,pseudo=courriel,type_utilisateur="passager")
                newUtilisateur.set_password(mdp)
                newUtilisateur.save()
                newPassager = Passager()
                newPassager.utilisateur = newUtilisateur
                newPassager.taille = int(taille)
                newPassager.save()
                messages.success(request, "Compte Passager crée avec succès")
                return redirect("inscription_passager")
        else:
            return render(request, "inscription-passager.html", {"form":form})

    else:
        return redirect("inscription_passager")
    

def valider_inscription_chauffeur(request:HttpRequest):
    if request.method == "POST":
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            courriel = data["courriel"]
            nom = data["nom"]
            prenom = data["prenom"]
            mdp = data["mdp"]
            numero_permis = data["numero_permis"]
            immatriculation = data["immatriculation"]
            couleur_voiture = data["couleur_voiture"] 
            marque_voiture = data["marque_voiture"] 
            annee_voiture = data["annee_voiture"] 
            courriel = str(courriel).lower()
            try:
                utilisateurExistant = Utilisateur.objects.get(pseudo=courriel)
                messages.info(request, "Un compte utilisateur existe déjà avec le même courriel")
                return redirect("inscription_chauffeur")
            except:
                newUtilisateur = Utilisateur(nom=nom,prenom=prenom,pseudo=courriel,type_utilisateur="chauffeur")
                newUtilisateur.set_password(mdp)
                newUtilisateur.save()
                newChauffeur = Chauffeur()
                newChauffeur.numero_permis = numero_permis
                newChauffeur.immatriculation = immatriculation
                newChauffeur.couleur_voiture = couleur_voiture
                newChauffeur.marque_voiture = marque_voiture
                newChauffeur.annee_voiture = int(annee_voiture)
                newChauffeur.utilisateur = newUtilisateur
                newChauffeur.save()
                messages.success(request, "Compte Chauffeur crée avec succès")
                return redirect("inscription_chauffeur")
        else:
            return render(request, "inscription-chauffeur.html", {"form":form})

    else:
        return redirect("inscription_chauffeur")
    

def valider_connexion(request:HttpRequest):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            courriel = data["courriel"]
            mdp = data["mdp"]
            courriel = str(courriel).lower()

            user = authenticate(request, pseudo=courriel, password=mdp)

            if user is None:
                messages.info(request, "Les informations saisies sont incorrectes")
                return redirect("connexion")
            
            login(request, user)

            if user.type_utilisateur == "chauffeur":
                return redirect("Dashboard:chauffeur")
            elif user.type_utilisateur == "passager":
                return redirect("Dashboard:passager")
            else:
                return redirect("index")
            
        else:
            return render(request, "connexion.html", {"form":form})
    else:
        return redirect("connexion")
    

def deconnexion(request):
    logout(request)
    messages.info(request, "Vous avez bien été déconnecté")
    return redirect("connexion")

