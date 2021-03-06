import datetime
# from datetime import date

# import socket

import geocoder
import cv2
# import numpy as np
# import pyzbar.pyzbar as pyzbar

# from django.contrib import auth
# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
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


# Inscription - Connexion - Déconnexion
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
                messages.error(request, "Le PSEUDO est déjà pris !", extra_tags='alert')
            elif Utilisateur.objects.filter(Mail=mail).exists():
                messages.error(request, "Erreur d'Adresse Mail", extra_tags='alert')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
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
                messages.success(request, "Utilisateur créé avec succès !", extra_tags='alert')
        else:
            messages.error(request, "Les mots de passe ne correspondent pas!", extra_tags='alert')
        return redirect('connexion')

    else:
        template = loader.get_template('dashoard/register.html')
        return HttpResponse(template.render(request=request))


def login(request):
    template = loader.get_template('dashoard/login.html')
    if request.method == 'POST':
        Myusername = request.POST.get('username')
        Mypassword = request.POST.get('password')
        user = authenticate(username=Myusername, password=Mypassword)
        if user:
            request.session["user_id"] = user.id
            nom = Utilisateur.objects.get(user_id_id=user.id).Nom
            prenom = Utilisateur.objects.get(user_id_id=user.id).Prenom
            admin = Utilisateur.objects.get(user_id_id=user.id).admin
            Count = Notes_Internes.objects.filter(Date=datetime.date.today())
            print(Count)
            # Count1 = Presence.objects.get(date=datetime.date.today())
            # print(Count1)
            badgeCount = Count.count()
            print(badgeCount)
            request.session["count"] = badgeCount
            # request.session["count1"] = Count1
            request.session["nom"] = nom
            request.session["prenom"] = prenom
            request.session["admin"] = admin
            print("You're logged in !")
            messages.success(request, "Connecté(e)", extra_tags='alert')
            return redirect('espace utilisateur')
            # return render(request, 'dashoard/index.html', {'popup': message})
        else:
            return redirect('erreur')
    else:
        return HttpResponse(template.render(request=request))


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('accueil')


def home(request):
    template = loader.get_template('dashoard/login.html')
    return HttpResponse(template.render(request=request))


#                                             D_A_S_B_O_A_R_D  U_T_I_L_I_S_A_T_E_U_R

# Notes de Service
def userDashboard(request):
    lstNotes = Notes_Internes.objects.all().order_by('-Date')
    return render(request, 'dashoard/index.html', {'listeNotes': lstNotes})


# Faire la présence
def qrscan(request):
    # Get user's position : lon and lat
    g = geocoder.ip('me')
    Ucoord = g.latlng

    cap = cv2.VideoCapture(-1)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:
                try:
                    # convert data (string) into data(list)
                    data = data.split(',')
                    # convert new data's content into float
                    data[0] = float(data[0])
                    data[1] = float(data[1])
                except KeyError:
                    cap.release()
                    cv2.destroyAllWindows()
                    return redirect('erreur')
                break
        # display the result
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    if Ucoord[0] == data[0] and Ucoord[1] == data[1]:
        cap.release()
        cv2.destroyAllWindows()
        arrivee = datetime.datetime.now().time()
        print(arrivee)
        heure = datetime.time(8, 00, 00, 00)
        print(heure)
        emp_id = request.session["user_id"]
        emp = Utilisateur.objects.get(user_id=emp_id).Matricule
        pres = Presence.objects.create(heureArrivee=arrivee, employe_id=emp, date=datetime.date.today)
        print(str(pres.employe) + " " + str(pres.heureArrivee) + " " + str(pres.debutPause) + " " + str(pres.finPause) + " " + str(pres.heureDepart) + " " + str(pres.statut))
        dif = heure - arrivee
        print(str(dif))
        if arrivee <= heure:
            Presence.objects.filter(heureArrivee=arrivee, employe_id=emp, date=datetime.date.today()).update(statut="Présent ! (À l'heure)")
        elif arrivee > heure:
            Presence.objects.filter(heureArrivee=arrivee, employe_id=emp, date=datetime.date.today()).update(statut="Présent ! (En retard)")
        print(str(pres.employe) + " " + str(pres.heureArrivee) + " " + str(pres.debutPause) + " " + str(pres.finPause) + " " + str(pres.heureDepart) + " " + str(pres.statut))
        # Redirection to userspace
        return redirect('espace utilisateur')
    else:
        return redirect('scan qr')


# Marquer le début de la pause
def PauseDej_Debut(request):
    debut = datetime.datetime.now()
    jour = datetime.date.today()
    emp_id = request.session["user_id"]
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    Presence.objects.filter(employe_id=emp, date=jour).update(debutPause=debut)
    return redirect('espace utilisateur')


# Marquer la fin de la pause
def PauseDej_Fin(request):
    fin = datetime.datetime.now()
    jour = datetime.date.today()
    emp_id = request.session["user_id"]
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    Presence.objects.filter(employe_id=emp, date=jour).update(finPause=fin)
    return redirect('espace utilisateur')


# Marquer le départ du service
def Depart(request):
    depart = datetime.datetime.now()
    jour = datetime.date.today()
    emp_id = request.session["user_id"]
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    Presence.objects.filter(employe_id=emp, date=jour).update(heureDepart=depart)
    return redirect('espace utilisateur')


# Demander une permission
def demandePermis(request):
    if request.method == 'POST':
        dateP = datetime.datetime.now()
        # permis = request.POST['permis']
        emp_id = request.session["user_id"]
        emp = Utilisateur.objects.get(user_id=emp_id).Matricule
        dateDebut = request.POST['dateDebut']
        heureDebut = request.POST['heureDebut']
        dateFin = request.POST['dateFin']
        heureFin = request.POST['heureFin']
        motif = request.POST['motif']
        dateDebut = datetime.datetime.strptime(dateDebut, '%Y-%m-%d')

        if dateDebut >= dateP + datetime.timedelta(days=2):
            permission = Permission.objects.create(Permissionnaire_id=emp, Date_Permission=dateP,
                                                   Date_Debut=dateDebut, heure_Debut=heureDebut,
                                                   Date_Fin=dateFin, heure_Fin=heureFin, Motif=motif)
            permission.save()
            messages.success(request, 'Demande envoyée avec succes !', extra_tags='alert')
        else:
            messages.error(request, "Erreur!!! La permission doit être demandée trois (03) jours plus tôt.", extra_tags='alert')
            # page = loader.get_template('dashoard/permissionForm.html')
            # return HttpResponse(page.render(request=request))
    permissionnaire = Utilisateur.objects.only("Matricule", "Nom", "Prenom")
    return render(request, 'dashoard/permissionForm.html', {'permissionnaire': permissionnaire})


# Historique des Permissions
def conges(request):
    emp_id = request.session["user_id"]
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    con = Permission.objects.order_by('Date_Permission').filter(Permissionnaire_id=emp, Status="Accordée")
    return render(request, 'dashoard/mes_conges.html', {'conges': con})


#                                             D_A_S_B_O_A_R_D  A_D_M_I_N_I_S_T_R_A_T_E_U_R

# Tableau de Présence
def tablePresence(request):
    liste = Presence.objects.all().order_by('date', 'heureArrivee')
    return render(request, 'dashoard/pointPresence.html', {'listeP': liste})


# Tableau des Demandes de Permission
def Listpermissions(request):
    permis = Permission.objects.all().order_by('-Code_Permission')
    return render(request, 'dashoard/permissions.html', {'listePermis': permis})


# Valider la demande de Permission
def Accepter(request, pk):
    Permission.objects.filter(Code_Permission=pk).update(Status="Accordée")
    messages.success(request, "Permission accordée avec succès !", extra_tags='alert')
    return redirect('permissions')


# Rejeter la demande de Permission
def Rejeter(request, pk):
    Permission.objects.filter(Code_Permission=pk).update(Status="Rejetée")
    messages.success(request, "Permission rejetée !", extra_tags='alert')
    return redirect('permissions')


# Ajouter un Employé ou un Stagiaire
def addEmploye(request):
    template = loader.get_template('dashoard/addemployee.html')
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
                messages.error(request, "Le PSEUDO est déjà pris !", extra_tags='alert')
            elif Utilisateur.objects.filter(Mail=mail).exists():
                messages.error(request, "Erreur d'Adresse Mail !", extra_tags='alert')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
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
                messages.success(request, "Employé(e) bien ajouté(e) !", extra_tags='alert')
                return redirect('espace utilisateur')
        else:
            messages.error(request, "Les mots de passe ne correspondent pas!", extra_tags='alert')
        return redirect('ajouter Employe')
    return HttpResponse(template.render(request=request))


# Formulaire d'ajout de Note de Service
def notesform(request):
    page = loader.get_template('dashoard/service-notes.html')
    return HttpResponse(page.render(request=request))


# Traitement d'ajout de la Note de Service
def notes(request):
    if request.method == 'POST':
        code = request.POST['codenote']
        titre = request.POST['titre']
        contenu = request.POST['contenu']
        note = Notes_Internes.objects.create(Code_Note=code, Titre=titre, Contenu=contenu)
        note.save()
        messages.success(request, "La note a bien été envoyée !", extra_tags='alert')
    else:
        messages.error(request, "Quelque chose s'est mal passé :(", extra_tags='alert')
    return redirect('espace utilisateur')


def utilisateurs(request):
    users = Utilisateur.objects.all()
    return HttpResponse(users)


def page404(request):
    page = loader.get_template('dashoard/404.html')
    return HttpResponse(page.render(request=request))


def error(request):
    page = loader.get_template('errorpages/wrong.html')
    return HttpResponse(page.render(request=request))


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


def CodeQR(request):
    page = loader.get_template('dashoard/qrcode.html')
    return HttpResponse(page.render(request=request))


def affichageBouton(request):
    emp_id = request.session["user_id"]
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    cond = Presence.objects.get(employe_id=emp, date=datetime.date.today)
    return render(request, 'dashoard/qrcode.html', {'cond': cond})


# Profile de l'utilisateur
def profile(request):
    emp_id = request.session["user_id"]
    usr = User.objects.get(id=emp_id)
    emp = Utilisateur.objects.get(user_id=emp_id)
    anniv = str(emp.DateDeNaissance).split('-', 3)
    entree = str(emp.Date_Entree).split('-', 3)
    sortie = str(emp.Date_Sortie).split('-', 3)
    return render(request, 'dashoard/profile.html', {'user': emp, 'usr': usr, 'anniv': anniv, 'entree': entree, 'sortie': sortie})


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
