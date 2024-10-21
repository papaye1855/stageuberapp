from django.db import models
from utilisateur.models import Utilisateur
from .constants import VOITURE_COULEUR_CHOICES, VOITURE_MARQUE_CHOICES
# Create your models here.

class Passager(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    taille = models.PositiveIntegerField(default=150)
    coordonnees = models.JSONField(default=list, blank=True)

    def __str__(self) -> str:
        return "Compte passager de " + self.utilisateur.prenom + " " + self.utilisateur.nom


class Chauffeur(models.Model):
    numero_permis = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=255)
    couleur_voiture = models.CharField(max_length=255,choices=VOITURE_COULEUR_CHOICES,default="blanche")
    marque_voiture = models.CharField(max_length=255,choices=VOITURE_MARQUE_CHOICES, default="hundai")
    annee_voiture = models.PositiveIntegerField()
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    coordonnees = models.JSONField(default=list, blank=True)

    def __str__(self) -> str:
        return "Compte chauffeur de " + self.utilisateur.prenom + " " + self.utilisateur.nom + " avec le permis de conduire N° : " + self.numero_permis



