from django.db import models
from django.utils import timezone


# Create your models here.

# LA TABLE UTILISATEUR
class Utilisateur(models.Model):
    #############################################################
    #                       UTILISATEUR                         #
    #############################################################
    Matricule = models.UUIDField(max_length=10, primary_key=True, unique=True, blank=False, auto_created=True)
    Nom = models.CharField(max_length=20, blank=False)
    Prenom = models.CharField(max_length=50, blank=False)
    Sexe = models.CharField(max_length=1, choices=('M', 'F'), blank=False)
    DateDeNaissance = models.DateField()
    Adresse = models.CharField(blank=False)
    Mail = models.EmailField(blank=False)
    Pays = models.CharField(blank=False)
    Ville = models.CharField(blank=False)
    Mobile = models.CharField(blank=False)
    Superviseur = models.CharField(blank=True)
    Pseudo = models.CharField(max_length=10, blank=False, unique=True)
    MotDePasse = models.CharField(max_length=10, blank=False, unique=True)
    Type_Utilisateur = models.CharField(choices=('Stagiaire', 'Employé'), blank=False)

    #############################################################
    #                         STAGIAIRE                         #
    #############################################################
    Filiere = models.CharField(max_length=20, blank=True)
    CV_lien = models.CharField(blank=True)
    LettreDeRecommandation_Lien = models.CharField(blank=True)
    LettreDeMotivation_Lien = models.CharField(blank=True)

    #############################################################
    #                         EMPLOYE                           #
    #############################################################
    CIN = models.PositiveIntegerField(blank=True)
    Status_matrimoniel = models.CharField(choices=('Célibataire', 'En couple', 'Marié(e)', 'Divorcé(e)'), blank=True)
    Enfants = models.PositiveIntegerField(blank=True)
    Telephone_Fixe = models.CharField()
    Departement = models.CharField(choices=..., blank=True)
    Fonction = models.CharField(choices=..., blank=True)
    Type_de_Contrat = models.CharField(choices=..., blank=True)
    Date_Entree = models.DateField(blank=True)
    Date_Sortie = models.DateField(blank=True)
    Nom_Contact_dUrgence = models.CharField()
    Telephone_Contact_dUrgence = models.CharField()

    # Les Méthodes sur le table UTILISATEUR


##################################################################################
#                                  PERMISSION                                    #
##################################################################################
class Permission(models.Model):
    Code_Permission = models.CharField(primary_key=True, auto_created=True)
    Date_Permission = models.DateTimeField(auto_created=True, default=timezone.now)
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    Motif = models.CharField()
    Status = models.CharField(choices=('Accordée', 'En attente', 'Refuser'))


###################################################################################
#                                 NOTES INTERNES                                  #
###################################################################################
class Notes_Internes(models.Model):
    Code_Note = models.CharField(blank=False, primary_key=True)
    Destinateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING)
    Destinataire = models.ManyToManyField(Utilisateur)
    Titre = models.CharField(blank=True, max_length=200)
    Contenu = models.TextField(max_length=2500)


################################################################
#                            CONGES                            #
################################################################
class Conge(models.Model):
    Code_Conge = models.CharField(primary_key=True, blank=False)
    Type_Conge = models.CharField(choices=('Congés Spéciaux', 'Congés maladie', 'Repos Sanitaire', 'Personnel', 'Congés annuels', 'Reprise jours fériés'), blank=False)


##########################################
#           CALENDRIER CONGES            #
##########################################
class Calendrier_Conge(models.Model):
    Date_Conge = models.DateField()


########################################################################
#                           PRENDRE CONGES                             #
########################################################################
class Prendre_Conge(models.Model):
    employe = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    conge = models.ForeignKey(Conge, on_delete=models.CASCADE)
    date = models.ForeignKey(Calendrier_Conge, on_delete=models.CASCADE)
    Duree = models.PositiveIntegerField()
    Status = models.CharField(choices=('En attente', 'Accordé', 'Rejeté'))

