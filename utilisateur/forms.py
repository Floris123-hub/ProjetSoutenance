from django import forms
from .models import Utilisateur, User


class InfosPerso(forms.ModelForm):
    class Meta:
        model = Utilisateur

        fields = [
            'Nom',
            'Prenom',
            'Sexe',
            'DateDeNaissance',
        ]

        labels = {
            'Nom': 'Nom',
            'Prenom': 'Prénom(s)',
            'Sexe': 'Sexe',
            'DateDeNaissance': 'Date de Naissance',
        }


class InfosAdresse(forms.ModelForm):
    class Meta:
        model = Utilisateur

        fields = [
            'Adresse',
            'Ville',
            'Pays',
            'Mail',
            'Mobile',
            'Nom_Contact_dUrgence',
            'Telephone_Contact_dUrgence',
        ]

        labels = {
            'Adresse': 'Adresse de résidence',
            'Ville': 'Ville de résidence',
            'Pays': 'Pays de Résidence',
            'Mail': 'E-mail',
            'Mobile': 'Téléphone',
            'Nom_Contact_dUrgence': "Nom du Contact",
            'Telephone_Contact_dUrgence': "Téléphone du contact",
        }


class InfosStagiairePro(forms.ModelForm):
    class Meta:
        model = Utilisateur

        fields = [
            'CIN',
            'Status_matrimoniel',
            'Enfants',
            'Telephone_Fixe',
            'Departement',
            'Fonction',
            'Lettre_Demande_Emploi',
        ]

        labels = {
            'CIN': "N° Carte d'identité nationale",
            'Status_matrimoniel': "Status matrimoniel",
            'Enfants': "Nombre d'enfants",
            'Telephone_Fixe': "Téléphone fixe",
            'Departement': "Département",
            'Fonction': "Fonction",
            'Lettre_Demande_Emploi': "Lettre de Demande d'emploi",
        }


class InfosStagiaireAcad(forms.ModelForm):
    class Meta:
        model = Utilisateur

        fields = [
            'Filiere',
            'CV',
            'LettreDeRecommandation',
            'LettreDeMotivation',
        ]

        labels = {
            'Filiere': 'Filière',
            'CV': 'CV',
            'LettreDeRecommandation': 'Lettre de Recommandation',
            'LettreDeMotivation': 'Lettre de Motivation',
        }


class InfosLogin(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'username',
            'password'
        ]

        labels = {
            'username': "Nom d'utilisateur",
            'password': "Mot de passe"
        }
