from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UtilisateurManager

UTILISATEUR_TYPES_CHOICES = (
    ("administration_membre", "Membre d'administration"),
    ('chauffeur', "Chauffeur"),
    ('passager', "Passager")
)

# Create your models here.

class Utilisateur(AbstractBaseUser, PermissionsMixin):
    nom = models.CharField(_("Nom"),max_length=255)
    prenom = models.CharField(_("Prenom"),max_length=255)
    pseudo = models.EmailField(_("Courriel Personnel"),unique=True)
    type_utilisateur = models.CharField(max_length=255, choices=UTILISATEUR_TYPES_CHOICES, default="passager")
    is_active = models.BooleanField(_("Compte Actif"),default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()


    USERNAME_FIELD = 'pseudo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")

