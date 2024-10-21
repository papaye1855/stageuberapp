from django.http.response import HttpResponse ,JsonResponse
from django.shortcuts import render
from dashboard.forms import PassagerForm , ChauffeurForm, ConnexionForm
from dashboard.models import Chauffeur
from django.views.decorators.csrf import csrf_exempt

import pusher

pusher_client = pusher.Pusher(
  app_id='1861464',
  key='b63a75edcfdfdd037332',
  secret='98943a1494ca8e5961af',
  cluster='us2',
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


def inscription_passager(request):
    form = PassagerForm()
    return render(request, "inscription-passager.html", {"form":form})


def inscription_chauffeur(request):
    form = ChauffeurForm()
    return render(request, "inscription-chauffeur.html",{"form":form})


def connexion(request):
    form = ConnexionForm()
    return render(request, "connexion.html", {"form":form})


def avoir_chauffeur(request):
    if request.method == "GET":
        chauffeurs = Chauffeur.objects.select_related("utilisateur").all()
        chauffeursMap = []
        for chauffeur in chauffeurs:
            chauffeurFeature = {
                "type" : "Feature",
                "properties" : {
                    "id" : chauffeur.pk,
                    "nom" : chauffeur.utilisateur.nom,
                    "prenom" : chauffeur.utilisateur.prenom,
                    "nomComplet" : f"{chauffeur.utilisateur.prenom} {chauffeur.utilisateur.nom}",
                    "immatriculationVoiture" : chauffeur.immatriculation,
                    "couleurVoiture" : str(chauffeur.couleur_voiture).capitalize(),
                    "anneeVoiture": chauffeur.annee_voiture,
                    "marqueVoiture":str(chauffeur.marque_voiture).capitalize()
                },
                "geometry" : {
                    "type" : "Point",
                    "coordinates": chauffeur.coordonnees 
                }
            }
            chauffeursMap.append(chauffeurFeature)
        data = {
            "type" : "FeatureCollection",
            "features" : chauffeursMap
        }

        return JsonResponse(data)
    else:
        return JsonResponse({})

@csrf_exempt    
def notifier_commande_course(request):
    if request.method == "POST":
        data = request.POST
        chauffeurSSE = data.get("chauffeurSSE")
        passagerNomComplet = data.get("passagerNomComplet")

        messageCustom = f"Le passager : {passagerNomComplet} souhaite faire un trajet"
        messageCustom += "pour aller à l'adresse : 1566 Avenue Berger, Montreal, QC, H1S8R5"

        pusher_client.trigger(chauffeurSSE, 'nouvelle-course', 
            {'message': messageCustom, 'prixCourse': "35 $CAD", "distance" : "16 KM"}
        )
        return JsonResponse(data={"message": "Tout est bon"})
    else:
        return JsonResponse(data={"message": "Non autorisé"})
    

@csrf_exempt    
def notifier_course_chat_message(request):
    if request.method == "POST":
        data = request.POST
        chauffeurSSE = data.get("chauffeurSSE")
        passagerNomComplet = data.get("passagerNomComplet")
        messagePassager = data.get("messagePassager")

        pusher_client.trigger(chauffeurSSE, 'nouveau-message', 
            {'message': messagePassager, "passagerNomComplet" : passagerNomComplet}
        )
        return JsonResponse(data={"message": "Tout est bon"})
    else:
        return JsonResponse(data={"message": "Non autorisé"})