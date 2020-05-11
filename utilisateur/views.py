# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
from django.template import loader
from django.http import HttpResponse

#  from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework import permissions
# from utilisateur.serializers import UserSerializer, GroupSerializer
from .models import Utilisateur, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes
from .serializers import UtilisateurSerializer, PermissionSerializer, CongesSerializer, Calendrier_CongeSerializer, Prendre_CongeSerializer, Notes_InternesSerializer


# Create your views here.


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]

class UtilisateurViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Utilisateur to be viewed or edited.
    """
    queryset = Utilisateur.objects.all().order_by('Nom')
    serializer_class = UtilisateurSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Permission to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CongesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Conges to be viewed or edited.
    """
    queryset = Conges.objects.all()
    serializer_class = CongesSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class Calendrier_CongeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Calendrier_Conge to be viewed or edited.
    """
    queryset = Calendrier_Conge.objects.all()
    serializer_class = Calendrier_CongeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class Prendre_CongeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Prendre_Conge to be viewed or edited.
    """
    queryset = Prendre_Conge.objects.all()
    serializer_class = Prendre_CongeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class Notes_InternesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Notes_Internes to be viewed or edited.
    """
    queryset = Notes_Internes.objects.all()
    serializer_class = Notes_InternesSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request))