from django.contrib import admin
from .models import Utilisateur
from django.contrib.auth.admin import UserAdmin
from .forms import UtilisateurCreationForm, UtilisateurChangeForm
# Register your models here.


class UtilisateurAdmin(UserAdmin):
    add_form = UtilisateurCreationForm
    form = UtilisateurChangeForm
    model = Utilisateur

    list_display = ('pseudo', 'nom', 'prenom', 'is_active', 'is_superuser','type_utilisateur')
    list_filter = ('pseudo', 'is_active', 'is_superuser','type_utilisateur')

    fieldsets = (
        (None, {"fields" : ("nom", "prenom", "pseudo", "password")}),
        ("Permissions", {"fields" : ("type_utilisateur", "is_staff", "is_active", "is_superuser", "groups", "user_permissions")})
    )
    

    add_fieldsets = (
        (None,{
            "classes" : ("wide",),
            "fields" : (
                "nom", "prenom", "password1", "password2" , "type_utilisateur" , "is_staff",
                "is_active", "is_superuser", "groups", "user_permissions"
            )
        }),
    )

    search_fields = ("pseudo",)
    ordering = ("pseudo", "type_utilisateur")


admin.site.register(Utilisateur , UtilisateurAdmin)
