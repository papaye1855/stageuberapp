from django import forms
from .models import Passager , Chauffeur


class PassagerForm(forms.ModelForm):
    nom = forms.CharField(max_length=255)
    prenom = forms.CharField(max_length=255)
    courriel = forms.EmailField()
    mdp = forms.CharField(widget=forms.PasswordInput(attrs={"type": "password"}))


    class Meta:
        model = Passager
        fields = ["taille"]


class ChauffeurForm(forms.ModelForm):
    nom = forms.CharField(max_length=255)
    prenom = forms.CharField(max_length=255)
    courriel = forms.EmailField()
    mdp = forms.CharField(widget=forms.PasswordInput(attrs={"type": "password"}))

    class Meta:
        model = Chauffeur
        fields = ["numero_permis","immatriculation","couleur_voiture","marque_voiture","annee_voiture"]


class ConnexionForm(forms.Form):
    courriel = forms.EmailField()
    mdp = forms.CharField(widget=forms.PasswordInput(attrs={"type": "password"}))
