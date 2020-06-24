import datetime
from datetime import date

# import socket

import geocoder
import cv2
# import numpy as np
# import pyzbar.pyzbar as pyzbar

from django.contrib import auth
# from django.contrib.auth.decorators import login_required
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


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))


def login(request):
    template = loader.get_template('login.html')
    if request.method == 'POST':
        # context = {}
        Myusername = request.POST.get('username')
        # Mypassword = request.POST.get('password')
        user = User.objects.get(username=Myusername)
        if user:
            request.session["user_id"] = user.id
            nom = Utilisateur.objects.get(user_id_id=user.id).Nom
            prenom = Utilisateur.objects.get(user_id_id=user.id).Prenom
            # admin = Utilisateur.objects.get(user_id_id=user.id).admin
            request.session["nom"] = nom
            request.session["prenom"] = prenom
            # request.session["admin"] = admin

            # Personne = str(personne[0])
            # print(type(nom))
            # print(nom)
            # print(type(prenom))
            # print(prenom)
            # context["nom"] = nom
            # context["prenom"] = prenom
            # print(context["prenom"])
            return redirect('espace utilisateur')
            # if user.is_superuser == 1:
            #     return redirect('espace administateur')
            # else:
            #     return redirect('espace utilisateur')
        else:
            return redirect('erreur')
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
    try:
        del request.session['user_id']
    except KeyError:
        pass
    print("You're logged out.")
    return redirect('accueil')


def utilisateurs(request):
    users = Utilisateur.objects.all()
    return HttpResponse(users)


def Listpermissions(request):
    permis = Permission.objects.all()
    print(permis)
    return render(request, 'dashoard/permissions.html', {'listeP': permis})


def conges(request):
    con = Conges.objects.all()
    print(con)
    return render(request, 'dashoard/calendrier.html', {'conges': con})


def tablePresence(request):
    liste = Presence.objects.all().order_by('aujourdhui')
    print(type(liste))
    return render(request, 'dashoard/pointPresence.html', {'listeP': liste})


def userDashboard(request):
    lstNotes = Notes_Internes.objects.all()
    n = 1
    n += 1
    print(lstNotes)
    return render(request, 'dashoard/index.html', {'listeNotes': lstNotes, 'n': n})


def page404(request):
    page = loader.get_template('dashoard/404.html')
    return HttpResponse(page.render(request=request))


def error(request):
    page = loader.get_template('errorpages/wrong.html')
    return HttpResponse(page.render(request=request))


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
    return HttpResponse(template.render(request=request))


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
    if request.method == 'POST':
        dateP = date.today()
        permis = request.POST['permis']
        dateDebut = request.POST['dateDebut']
        heureDebut = request.POST['heureDebut']
        dateFin = request.POST['dateFin']
        heureFin = request.POST['heureFin']
        motif = request.POST['motif']

        permission = Permission.objects.create(Permissionnaire_id=permis, Date_Permission=dateP,
                                               Date_Debut=dateDebut, heure_Debut=heureDebut,
                                               Date_Fin=dateFin, heure_Fin=heureFin, Motif=motif)

        if permission.Date_Debut.day == permission.Date_Permission.day + 3:
            permission.save()
        else:
            print('Erreur !')
            print('La permission doit être demandée trois jours plus tôt !')
            page = loader.get_template('dashoard/permissionForm.html')
            return HttpResponse(page.render(request=request))
    else:
        permissionnaire = Utilisateur.objects.only("Matricule", "Nom", "Prenom")
        print(permissionnaire)
        return render(request, 'dashoard/permissionForm.html', {'permissionnaire': permissionnaire})


def CodeQR(request):
    page = loader.get_template('dashoard/qrcode.html')
    return HttpResponse(page.render(request=request))


def qrscan(request):
    # Get user's position : lon and lat
    g = geocoder.ip('me')
    Ucoord = g.latlng

    # # si la postion est bien récupérée
    # cap = cv2.VideoCapture(0)

    # while True:
    #     _, frame = cap.read()

    #     decodeObj = pyzbar.decode(frame)

    #     for obj in decodeObj:
    #         string = str(obj.data)
    #         ready = string.strip("b'")
    #         # print(ready)
    #         break

    #     cv2.imshow("Scanner", frame)

    #     key = cv2.waitKey(1)

    # # When everything is done, release the capture
    # cv2.destroyAllWindows()
    # cap.release()

    cap = cv2.VideoCapture(0)
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
                    # display it and it's type
                    print(data)
                    letype = type(data)
                    print(letype)
                    # convert new data's content into float
                    data[0] = float(data[0])
                    data[1] = float(data[1])
                except:
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
        arrivee = datetime.datetime.now()
        print(arrivee)
        emp_id = request.session["user_id"]
        print(emp_id)
        emp = Utilisateur.objects.get(user_id=emp_id).Matricule
        print(emp)
        Presence.objects.create(heureArrivee=arrivee, employe_id=emp)
        # Redirection to userspace
        return redirect('espace utilisateur')
    else:
        return redirect('scan qr')


def PauseDej_Debut(request):
    debut = datetime.datetime.now()
    print(debut)
    jour = datetime.datetime.today()
    emp_id = request.session["user_id"]
    print(emp_id)
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    print(emp)
    Presence.objects.filter(employe_id=emp, aujourdhui=jour).update(debutPause=debut)
    return redirect('espace utilisateur')


def PauseDej_Fin(request):
    fin = datetime.datetime.now()
    print(fin)
    jour = datetime.datetime.today()
    emp_id = request.session["user_id"]
    print(emp_id)
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    print(emp)
    Presence.objects.filter(employe_id=emp, aujourdhui=jour).update(finPause=fin)
    return redirect('espace utilisateur')


def Depart(request):
    depart = datetime.datetime.now()
    print(depart)
    jour = datetime.datetime.today()
    emp_id = request.session["user_id"]
    print(emp_id)
    emp = Utilisateur.objects.get(user_id=emp_id).Matricule
    print(emp)
    Presence.objects.filter(employe_id=emp, aujourdhui=jour).update(heureDepart=depart)
    return redirect('espace utilisateur')


def notesform(request):
    page = loader.get_template('dashoard/service-notes.html')
    return HttpResponse(page.render(request=request))


def notes(request):
    if request.method == 'POST':
        code = request.POST['codenote']
        titre = request.POST['titre']
        contenu = request.POST['contenu']
        note = Notes_Internes.objects.create(Code_Note=code, Titre=titre, Contenu=contenu)
        note.save()
    else:
        return redirect('erreur')
    return redirect('espace utilisateur')


# def listeNotes(request):
#     lstNotes = Notes_Internes.objects.all()
#     print(lstNotes)
#     return render(request, 'dashoard/index.html', {'listeNotes': lstNotes})


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
