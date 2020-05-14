from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Utilisateur, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes, Presence


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

        def create(self, validate_data):
            user = User.objects.create(**validate_data)
            Token.objects.create(user=user)
            return user


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
            'Photo',
            'Type_Utilisateur',
            'Filiere',
            'CV',
            'LettreDeRecommandation',
            'LettreDeMotivation',
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


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'
