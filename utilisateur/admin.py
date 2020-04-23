from django.contrib import admin

# Register your models here.

from .models import Utilisateur, Photo, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes

admin.site.register(Utilisateur)
admin.site.register(Photo)
admin.site.register(Permission)
admin.site.register(Conges)
admin.site.register(Calendrier_Conge)
admin.site.register(Prendre_Conge)
admin.site.register(Notes_Internes)
