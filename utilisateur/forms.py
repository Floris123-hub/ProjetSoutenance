from django import forms
from .models import Utilisateur


class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        widgets = {
            'MotDePasse': forms.PasswordInput()
        }
