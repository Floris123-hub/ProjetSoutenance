from django.db import models
from django.utils import timezone

# Create your models here.


# Choix de type d'utilisateur
CHOIX_TYPE_UTILISATEUR = (
    ('Stagiaire', 'Stagiaire'),
    ('Employé', 'Employé')
)


# Choix du sexe
CHOIX_SEXE = (
    ('M', 'M'),
    ('F', 'F')
)

#############################################################
#                       UTILISATEUR                         #
#############################################################
class Utilisateur(models.Model):
    Matricule = models.UUIDField(max_length=10, primary_key=True, unique=True, blank=False)
    Nom = models.CharField(max_length=20, blank=False)
    Prenom = models.CharField(max_length=50, blank=False)
    Sexe = models.CharField(max_length=1, choices=CHOIX_SEXE, blank=False)
    DateDeNaissance = models.DateField()
    Adresse = models.CharField(blank=False, max_length=255)
    Mail = models.EmailField(blank=False)
    Pays = models.CharField(blank=False, max_length=30)
    Ville = models.CharField(blank=False, max_length=30)
    Mobile = models.CharField(blank=False, max_length=20)
    Superviseur = models.CharField(blank=True, max_length=100)
    Pseudo = models.CharField(max_length=10, blank=False, unique=True)
    MotDePasse = models.CharField(max_length=10, blank=False, unique=True)
    Type_Utilisateur = models.CharField(choices=CHOIX_TYPE_UTILISATEUR, blank=False, max_length=10)

    #############################################################
    #                         STAGIAIRE                         #
    #############################################################
    Filiere = models.CharField(max_length=20, blank=True)
    CV_lien = models.FilePathField(blank=True)
    LettreDeRecommandation_Lien = models.FilePathField(blank=True)
    LettreDeMotivation_Lien = models.FilePathField(blank=True)

    # Choix Status Matrimoniel
    CHOIX_SITUATION_MATRIMONIEL = (
        ('Célibataire', 'Célibataire'),
        ('En couple', 'En couple'),
        ('Marié(e)', 'Marié(e)'),
        ('Divorcé(e)', 'Divorcé(e)')
    )

    #############################################################
    #                         EMPLOYE                           #
    #############################################################
    CIN = models.PositiveIntegerField(blank=True)
    Status_matrimoniel = models.CharField(choices=CHOIX_SITUATION_MATRIMONIEL, blank=True, max_length=10)
    Enfants = models.PositiveIntegerField(blank=True)
    Telephone_Fixe = models.CharField(max_length=20)
    Departement = models.CharField(choices=..., blank=True, max_length=30)
    Fonction = models.CharField(choices=..., blank=True, max_length=30)
    Type_de_Contrat = models.CharField(choices=..., blank=True, max_length=20)
    Date_Entree = models.DateField(blank=True)
    Date_Sortie = models.DateField(blank=True)
    Nom_Contact_dUrgence = models.CharField(max_length=30)
    Telephone_Contact_dUrgence = models.CharField(max_length=50)


#############################################################
#                          PHOTOS                           #
#############################################################
class Photo(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Photo_Id = models.CharField(primary_key=True, blank=False, max_length=10)
    Photo_Lien = models.FilePathField()


# Choix status permission
STATUS_PERMISSION = (
    ('Accordée', 'Accordée'),
    ('En attente', 'En attente'),
    ('Refuser', 'Refuser')
)


##################################################################################
#                                  PERMISSION                                    #
##################################################################################
class Permission(models.Model):
    Code_Permission = models.CharField(primary_key=True, max_length=10)
    Permissionnaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Date_Permission = models.DateTimeField(default=timezone.now)
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    Motif = models.CharField(max_length=50)
    Status = models.CharField(choices=STATUS_PERMISSION, max_length=10)


###################################################################################
#                                 NOTES INTERNES                                  #
###################################################################################
class Notes_Internes(models.Model):
    Code_Note = models.CharField(blank=False, primary_key=True, max_length=30)
    Destinateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING, related_name='Destinateur')
    Destinataire = models.ManyToManyField(Utilisateur, related_name='Destinataire')
    Titre = models.CharField(blank=True, max_length=200)
    Contenu = models.TextField(max_length=2500)


# Choix des types de congés
CHOIX_TYPE_CONGES = (
    ('Congés Spéciaux', 'Congés Spéciaux'),
    ('Congés maladie', 'Congés maladie'),
    ('Repos Sanitaire', 'Repos Sanitaire'),
    ('Personnel', 'Personnel'),
    ('Congés annuels', 'Congés annuels'),
    ('Reprise jours fériés', 'Reprise jours fériés')
)


################################################################
#                            CONGES                            #
################################################################
class Conges(models.Model):
    Code_Conges = models.CharField(primary_key=True, blank=False, max_length=5)
    Type_Conges = models.CharField(choices=CHOIX_TYPE_CONGES, blank=False, max_length=50)


##########################################
#           CALENDRIER CONGES            #
##########################################
class Calendrier_Conge(models.Model):
    Date_Conge = models.DateField()


# Statut de la demande de congés
STATUS_CONGES = (
    ('En attente', 'En attente'),
    ('Accordé', 'Accordé'),
    ('Rejeté', 'Rejeté')
)


########################################################################
#                           PRENDRE CONGES                             #
########################################################################
class Prendre_Conge(models.Model):
    employe = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    conges = models.ForeignKey(Conges, on_delete=models.CASCADE)
    date = models.ForeignKey(Calendrier_Conge, on_delete=models.CASCADE)
    Duree = models.PositiveIntegerField()
    Status = models.CharField(choices=STATUS_CONGES, max_length=10)
