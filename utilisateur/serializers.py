from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Utilisateur, Photo, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'Matricule',
            'Nom',
            'Prenom',
            'Sexe',
            'DateDeNaissance',
            'Adresse',
            'Mail',
            'Pays',
            'Ville',
            'Mobile',
            'Superviseur',
            'Pseudo',
            'MotDePasse',
            'Type_Utilisateur',
            'Filiere',
            #'CV_lien',
            # 'LettreDeRecommandation_Lien',
            # 'LettreDeMotivation_Lien',
            'CIN',
            'Status_matrimoniel',
            'Enfants',
            'Telephone_Fixe',
            'Departement',
            'Fonction',
            'Type_de_Contrat',
            'Date_Entree',
            'Date_Sortie',
            'Nom_Contact_dUrgence',
            'Telephone_Contact_dUrgence'
        ]


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'Photo_Id',
            'Photo_Lien',
            'utilisateur'
        ]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = [
            'Code_Permission',
            'Date_Permission',
            'Date_Debut',
            'Date_Fin',
            'Motif',
            'Status',
            'Permissionnaire'
        ]


class CongesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conges
        fields = [
            'Code_Conges',
            'Type_Conges'
        ]


class Calendrier_CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendrier_Conge
        fields = [
            'Date_Conge'
        ]


class Prendre_CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prendre_Conge
        fields = [
            'Duree',
            'Status',
            'conges',
            'date',
            'employe'
        ]


class Notes_InternesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes_Internes
        fields = [
            'Code_Note',
            'Destinateur',
            'Destinataire',
            'Titre',
            'Contenu'
        ]
