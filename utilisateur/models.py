from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from uuid import uuid4
# from passlib.hash import pbkdf2_sha256


id = str(datetime.datetime.now())
x = str(''.join(e for e in id if e.isalnum()))

photo = str(uuid4())
# Create your models here.


# Choix de type d'utilisateur
CHOIX_TYPE_UTILISATEUR = (
    ('Stagiaire Pro', 'Stagiaire Pro'),
    ('Stafiaire académique', 'Stagiaire académique')
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
    Matricule = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=x)
    Nom = models.CharField(max_length=50, blank=False, verbose_name="Nom *")
    Prenom = models.CharField(max_length=50, blank=False, verbose_name="Prénom(s) *")
    Sexe = models.CharField(max_length=1, choices=CHOIX_SEXE, blank=False, verbose_name="Sexe *")
    DateDeNaissance = models.DateField(verbose_name="Date de naissance *")
    Adresse = models.CharField(blank=False, max_length=255, verbose_name="Adresse *")
    Mail = models.EmailField(blank=False, verbose_name="E-mail *")
    Pays = models.CharField(blank=False, max_length=30, verbose_name="Pays *")
    Ville = models.CharField(blank=False, max_length=30, verbose_name="Ville *")
    Mobile = models.CharField(blank=False, max_length=20, unique=True, verbose_name="Téléphone *")
    Superviseur = models.CharField(blank=True, max_length=100)
    # Pseudo = models.CharField(max_length=10, blank=False, unique=True, verbose_name="Pseudo *", help_text="Votre pseudo pour votre authentification.")
    # MotDePasse = models.CharField(max_length=10, blank=False, unique=True, verbose_name="Mot de passe *", help_text="Mot de passe de connexion.")

    Photo = models.FileField(upload_to='Fichiers/photos', verbose_name="Photo *")
    Type_Utilisateur = models.CharField(choices=CHOIX_TYPE_UTILISATEUR, blank=False, max_length=50, verbose_name='Employé(e)/Stagiaire *')

    #############################################################
    #                         STAGIAIRE                         #
    #############################################################
    Filiere = models.CharField(max_length=50, blank=True, verbose_name="Filière *")
    CV = models.FileField(blank=True, upload_to='Fichiers/cv', verbose_name="Curriculum Vitae")
    LettreDeRecommandation = models.FileField(blank=True, upload_to='Fichiers/recommandations', verbose_name="Lettre de recommandation")
    LettreDeMotivation = models.FileField(blank=True, upload_to='Fichiers/motivations', verbose_name="Lettre de motivation")

    #############################################################
    #                         EMPLOYE                           #
    #############################################################
    CIN = models.CharField(blank=True, unique=True, max_length=7, help_text="Numéro de votre Carte d'Identité Nationale")
    Status_matrimoniel = models.CharField(choices=CHOIX_SITUATION_MATRIMONIEL, blank=True, max_length=20, verbose_name="Status matrimoniel")
    Enfants = models.PositiveIntegerField(blank=True, verbose_name="Enfant(s) *")
    Telephone_Fixe = models.CharField(max_length=20, blank=True, verbose_name="Téléphone fixe")
    Departement = models.CharField(choices=CHOIX_DEPARTEMENT, blank=False, max_length=50, verbose_name="Département *")
    Fonction = models.CharField(choices=CHOIX_FONCTION, blank=True, max_length=50)
    Lettre_Demande_Emploi = models.FileField(blank=True, upload_to="Fichiers/demandes d'emploi", verbose_name="Lettre de Demande d'Emploi")
    Type_de_Contrat = models.CharField(choices=TYPE_CONTRAT, blank=False, max_length=20)
    Date_Entree = models.DateField(blank=True, verbose_name="Date d'entrée *")
    Date_Sortie = models.DateField(blank=True, verbose_name="Date de sortie")
    Nom_Contact_dUrgence = models.CharField(max_length=30, verbose_name="Nom du Contact d'urgence")
    Telephone_Contact_dUrgence = models.CharField(max_length=50, verbose_name="Téléphone du contact d'urgence")

    def __str__(self):
        return self.Nom + " " + self.Prenom


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
    Code_Permission = models.CharField(primary_key=True, max_length=10, auto_created=True, editable=False)
    Permissionnaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    Date_Permission = models.DateTimeField(default=timezone.now)
    Date_Debut = models.DateField()
    Date_Fin = models.DateField()
    Motif = models.CharField(max_length=50)
    Status = models.CharField(choices=STATUS_PERMISSION, max_length=10)

    def __str__(self):
        return self.Code_Permission + " " + self.Permissionnaire


###################################################################################
#                                 NOTES INTERNES                                  #
###################################################################################
class Notes_Internes(models.Model):
    Code_Note = models.CharField(blank=False, primary_key=True, max_length=30)
    Destinateur = models.ForeignKey(Utilisateur, on_delete=models.DO_NOTHING, related_name='Destinateur')
    Destinataire = models.ManyToManyField(Utilisateur, related_name='Destinataire')
    Titre = models.CharField(blank=True, max_length=200)
    Contenu = models.TextField(max_length=2500)

    def __str__(self):
        return self.Code_Note + " " + self.Titre


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

    def __str__(self):
        return self.employe + " " + self.date


# STATUS DE LA PRESENCE
STATUS_PRESENCE = (
    ("avance", "En avance"),
    ("retard", "En retard")
)


########################################################################
#                           LES PRÉSENCES                              #
########################################################################
class Presence(models.Model):
    employe = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, verbose_name="Employé")
    heureArrivee = models.DateTimeField(verbose_name="Heure d'Arrivée")
    heureDepart = models.DateTimeField(verbose_name="Heure de Départ")
    status = models.CharField(max_length=100, choices=STATUS_PRESENCE)
    debutPause = models.DateTimeField(verbose_name="Heure de début de la Pause")
    finPause = models.DateTimeField(verbose_name="Heure de fin de la Pause")

    def __str__(self):
        return self.employe

