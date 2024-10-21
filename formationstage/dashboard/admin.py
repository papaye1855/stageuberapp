from django.contrib import admin
from .models import Passager, Chauffeur


admin.site.register([Passager, Chauffeur])

# Register your models here.
