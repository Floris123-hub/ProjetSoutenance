from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Utilisateur, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes, Presence


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class CongesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conges
        fields = '__all__'


class Calendrier_CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendrier_Conge
        fields = '__all__'


class Prendre_CongeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prendre_Conge
        fields = '__all__'


class Notes_InternesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes_Internes
        fields = '__all__'


class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presence
        fields = '__all__'
