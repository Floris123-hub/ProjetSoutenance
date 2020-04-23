from django.db import models
from django.utils import timezone
import datetime

id = str(datetime.datetime.now())
x = str(''.join(e for e in id if e.isalnum()))

id2 = str(datetime.date.today())
y = str(''.join(e for e in id2 if e.isalnum()))

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

# Choix Status Matrimoniel
CHOIX_SITUATION_MATRIMONIEL = (
    ('Célibataire', 'Célibataire'),
    ('En couple', 'En couple'),
    ('Marié(e)', 'Marié(e)'),
    ('Divorcé(e)', 'Divorcé(e)')
)

# Choix du département
CHOIX_DEPARTEMENT = (
    ('Direction', 'Direction'),
    ('Comptabilité', 'Service Comptable'),
    ('Ressources Humaines', 'Ressources Humaines'),
    ('Production et Développement', 'Production et Développement'),
    ('Informatique', 'Service Informatique'),
    ('Communication et Marketing', 'Communication et Marketing'),
    ('Commercial', 'Service Commercial'),
    ('Juridique', 'Service Juridique')

)

# Choix de la fonction
CHOIX_FONCTION = (
    # Pour le département informatique
    ('Dev Front', 'Développeur(euse) Front-End'),
    ('Dev Back', 'Développeur(euse) Back-End'),
    ('Dev Full', 'Développeur(euse) Full Stack'),
    ('Graphiste', 'Graphiste'),
    ('Maintenancier', 'Maintenancier'),

    # Pour le département de la Communication
    ('CM', 'Community Manager'),
    ('CC', 'Chargé(e) de Communication'),

    # Pour le département de la Comptabilité
    ('GC', 'Gestionnnaire Comptable'),
    ('AGC', 'Assistant(e) Gestionnaire Comptable'),
    ('Audit', 'Auditeur(trice)'),
    ('Commission', 'Commissaire aux comptes'),

    # Pour le département Juridique
    ('Juriste', 'Juriste'),

    # Pour le département des Ressources Humaines
    ('DRH', 'Directeur(trice) des Ressources Humaines'),
    ('ARH', 'Assistant(e) de direction des Ressources Humaines'),

    # Pour le service de la direction
    ('DG', 'Directeur(trice) Général(e)'),
    ('ADG', 'Assistant(e) de Direction Générale'),

    # Pour le service Commercial
    ('DC', 'Directeur(trice) Commercial(e)')
)

# Choix du type de contrat
TYPE_CONTRAT = (
    ('CDD', 'Contrat Durée Déterminée'),
    ('CDI', 'Contrat Durée Indéterminée'),
    ('CP', 'Contrat de Prestation'),
    ('CS', 'Convention de Stage')
)


#############################################################
#                       UTILISATEUR                         #
#############################################################
class Utilisateur(models.Model):
    Matricule = models.CharField(max_length=20, primary_key=True, unique=True, default=x, editable=False)
    Nom = models.CharField(max_length=20, blank=False)
    Prenom = models.CharField(max_length=50, blank=False)
    Sexe = models.CharField(max_length=1, choices=CHOIX_SEXE, blank=False)
    DateDeNaissance = models.DateField()
    Adresse = models.CharField(blank=False, max_length=255)
    Mail = models.EmailField(blank=False)
    Pays = models.CharField(blank=False, max_length=30)
    Ville = models.CharField(blank=False, max_length=30)
    Mobile = models.CharField(blank=False, max_length=20, unique=True)
    Superviseur = models.CharField(blank=True, max_length=100)
    Pseudo = models.CharField(max_length=10, blank=False, unique=True)
    MotDePasse = models.CharField(max_length=10, blank=False, unique=True)
    Type_Utilisateur = models.CharField(choices=CHOIX_TYPE_UTILISATEUR, blank=False, max_length=10)

    #############################################################
    #                         STAGIAIRE                         #
    #############################################################
    Filiere = models.CharField(max_length=50, blank=True)
    CV_lien = models.CharField(blank=True, max_length=100)
    LettreDeRecommandation_Lien = models.CharField(blank=True, max_length=100)
    LettreDeMotivation_Lien = models.CharField(blank=True, max_length=100)

    #############################################################
    #                         EMPLOYE                           #
    #############################################################
    CIN = models.PositiveIntegerField(blank=True, unique=True)
    Status_matrimoniel = models.CharField(choices=CHOIX_SITUATION_MATRIMONIEL, blank=True, max_length=20)
    Enfants = models.PositiveIntegerField(blank=True)
    Telephone_Fixe = models.CharField(max_length=20, blank=True)
    Departement = models.CharField(choices=CHOIX_DEPARTEMENT, blank=True, max_length=50)
    Fonction = models.CharField(choices=CHOIX_FONCTION, blank=True, max_length=50)
    Type_de_Contrat = models.CharField(choices=TYPE_CONTRAT, blank=True, max_length=20)
    Date_Entree = models.DateField(blank=True)
    Date_Sortie = models.DateField(blank=True)
    Nom_Contact_dUrgence = models.CharField(max_length=30)
    Telephone_Contact_dUrgence = models.CharField(max_length=50)


#############################################################
#                          PHOTOS                           #
#############################################################
class Photo(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, max_length=20, default=Utilisateur.Nom)
    Photo_Id = models.UUIDField(primary_key=True, max_length=20, auto_created=True)
    Photo_Lien = models.CharField(max_length=100)


# Choix status permission
STATUS_PERMISSION = (
    ('Accordée', 'Accordée'),
    ('En attente', 'En attente'),
    ('Refusée', 'Refusée')
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
    Code_Conges = models.CharField(primary_key=True, blank=False, max_length=10)
    Type_Conges = models.CharField(choices=CHOIX_TYPE_CONGES, blank=False, max_length=50)


##########################################
#           CALENDRIER CONGES            #
##########################################
class Calendrier_Conge(models.Model):
    Date_Conge = models.DateField(primary_key=True)


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
