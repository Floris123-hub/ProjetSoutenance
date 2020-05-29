from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

from django.contrib.auth.models import User, Group
from django.shortcuts import redirect, render
from django.template import loader
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from utilisateur.serializers import UserSerializer, GroupSerializer
from .models import Utilisateur, Permission, Conges, Calendrier_Conge, Prendre_Conge, Notes_Internes, Presence
from .serializers import UtilisateurSerializer, PermissionSerializer, CongesSerializer, Calendrier_CongeSerializer, \
    Prendre_CongeSerializer, Notes_InternesSerializer, PresenceSerializer


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class PresenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Presence to be viewed or edited
    """
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        Myusername = request.POST.get('username')
        user = User.objects.get(username=Myusername)
        if user:
            request.session["user_id"] = user.id
            return redirect('espace utilisateur')
            # if user.is_superuser == 1:
            #     return redirect('espace administateur')
            # else:
            #     return redirect('espace utilisateur')
        else:
            msg = "Somethig were wrong :("
            print(msg)
            return HttpResponse(msg)
    else:
        return HttpResponse(template.render(request=request))


def register(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenoms = request.POST['prenoms']
        sexe = request.POST['sexe']
        Dnaissance = request.POST['birthday']
        adresse = request.POST['adresse']
        mail = request.POST['email']
        ville = request.POST['ville']
        pays = request.POST['pays']
        mobile = request.POST['mobile']
        Curgent = request.POST['contactUrgence']
        TCurgent = request.POST['telUrgence']
        cin = request.POST['cin']
        statusMat = request.POST['statusMat']
        enfants = request.POST['enfants']
        fixe = request.POST['fixe']
        departement = request.POST['departement']
        fonction = request.POST['fonction']
        demande = request.POST['demande']
        filiere = request.POST['filiere']
        cv = request.POST['cv']
        recommandation = request.POST['recommandation']
        motivation = request.POST['motivation']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        username = request.POST['username']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                print('Le Pseudo est déjà pris !')
            elif Utilisateur.objects.filter(Mail=mail).exists():
                print('Email déjà pris !')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                print(str(user.id))
                utilisateur = Utilisateur.objects.create(Nom=nom, Prenom=prenoms, Sexe=sexe, DateDeNaissance=Dnaissance,
                                                         Adresse=adresse, Mail=mail, Ville=ville, Pays=pays,
                                                         Mobile=mobile,
                                                         Nom_Contact_dUrgence=Curgent,
                                                         Telephone_Contact_dUrgence=TCurgent,
                                                         CIN=cin, Status_matrimoniel=statusMat, Enfants=enfants,
                                                         Telephone_Fixe=fixe,
                                                         Departement=departement, Fonction=fonction,
                                                         Lettre_Demande_Emploi=demande,
                                                         Filiere=filiere, CV=cv, LettreDeRecommandation=recommandation,
                                                         LettreDeMotivation=motivation, user_id_id=user.id)
                utilisateur.save()
                print(utilisateur)
                print('Utilisateur créé !')
        else:
            print('Les mots de passe ne correspondent pas !')
        return redirect('connexion')

    else:
        template = loader.get_template('form.html')
        return HttpResponse(template.render(request=request))


def logout(request):
    auth.logout(request)
    return redirect('accueil')


def utilisateurs(request):
    users = Utilisateur.objects.all()
    return HttpResponse(users)


def permissions(request):
    permis = Permission.objects.all()
    return HttpResponse(permis)


def conges(request):
    con = Conges.objects.all()
    return HttpResponse(con)


def listePresence(request):
    liste = Presence.objects.filter('aujourdhui')
    return HttpResponse(liste)


def userDashboard(request):
    page = loader.get_template('dashoard/index.html')
    return HttpResponse(page.render(request=request))


def page404(request):
    page = loader.get_template('dashoard/404.html')
    return HttpResponse(page.render(request=request))


def addEmploye(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenoms = request.POST['prenoms']
        sexe = request.POST['sex']
        Dnaissance = request.POST['birthday']
        adresse = request.POST['adresse']
        mail = request.POST['email']
        ville = request.POST['ville']
        pays = request.POST['pays']
        mobile = request.POST['mobile']
        Curgent = request.POST['contactUrgence']
        TCurgent = request.POST['telUrgence']
        cin = request.POST['cin']
        statusMat = request.POST['statusMat']
        enfants = request.POST['enfants']
        fixe = request.POST['fixe']
        departement = request.POST['departement']
        fonction = request.POST['fonction']
        demande = request.POST['demande']
        filiere = request.POST['filiere']
        cv = request.POST['cv']
        recommandation = request.POST['recommandation']
        motivation = request.POST['motivation']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        username = request.POST['username']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                print('Le Pseudo est déjà pris !')
            elif Utilisateur.objects.filter(Mail=mail).exists():
                print('Adresse mail déjà utilisée !')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                print(str(user.id))
                utilisateur = Utilisateur.objects.create(Nom=nom, Prenom=prenoms, Sexe=sexe, DateDeNaissance=Dnaissance,
                                                         Adresse=adresse, Mail=mail, Ville=ville, Pays=pays,
                                                         Mobile=mobile,
                                                         Nom_Contact_dUrgence=Curgent,
                                                         Telephone_Contact_dUrgence=TCurgent,
                                                         CIN=cin, Status_matrimoniel=statusMat, Enfants=enfants,
                                                         Telephone_Fixe=fixe,
                                                         Departement=departement, Fonction=fonction,
                                                         Lettre_Demande_Emploi=demande,
                                                         Filiere=filiere, CV=cv, LettreDeRecommandation=recommandation,
                                                         LettreDeMotivation=motivation, user_id_id=user.id)
                utilisateur.save()
                print(utilisateur)
                print('Employé(e) bien ajouté(e) !')
                return redirect('espace utilisateur')
        else:
            print('Les mots de passe ne correspondent pas !')
        return redirect('ajouter Employe')


def blank(request):
    page = loader.get_template('dashoard/blank.html')
    return HttpResponse(page.render(request=request))


def buttons(request):
    page = loader.get_template('dashoard/buttons.html')
    return HttpResponse(page.render(request=request))


def cards(request):
    page = loader.get_template('dashoard/cards.html')
    return HttpResponse(page.render(request=request))


def charts(request):
    page = loader.get_template('dashoard/charts.html')
    return HttpResponse(page.render(request=request))


def forgotPass(request):
    page = loader.get_template('dashoard/forgot-password.html')
    return HttpResponse(page.render(request=request))


def demandePermis(request):
    permissionnaire = Utilisateur.objects.only("Matricule", "Nom", "Prenom")
    render(request, 'dashoard/permissionForm.html', {'permissionnaire': permissionnaire})
    if request.method == 'POST':
        dateDebut = request.POST['dateDebut']
        permis = request.POST['permis']
        heureDebut = request.POST['heureDebut']
        dateFin = request.POST['dateFin']
        heureFin = request.POST['heureFin']
        motif = request.POST['motif']

        permission = Permission.objects.create(Permissionnaire_id=permis, Date_Debut=dateDebut, heure_Debut=heureDebut, Date_Fin=dateFin, heure_Fin=heureFin, Motif=motif)
        permission.save()
    else:
        print('Erreur !')
    page = loader.get_template('dashoard/permissionForm.html')
    return HttpResponse(page.render(request=request))


def CodeQR(request):
    page = loader.get_template('dashoard/qrcode.html')
    return HttpResponse(page.render(request=request))


def notes(request):
    page = loader.get_template('dashoard/service-notes.html')
    return HttpResponse(page.render(request=request))


def tables(request):
    page = loader.get_template('dashoard/tables.html')
    return HttpResponse(page.render(request=request))


def animation(request):
    page = loader.get_template('dashoard/utilities-animation.html')
    return HttpResponse(page.render(request=request))


def border(request):
    page = loader.get_template('dashoard/utilities-border.html')
    return HttpResponse(page.render(request=request))


def color(request):
    page = loader.get_template('dashoard/utilities-color.html')
    return HttpResponse(page.render(request=request))


def other(request):
    page = loader.get_template('dashoard/utilities-other.html')
    return HttpResponse(page.render(request=request))
