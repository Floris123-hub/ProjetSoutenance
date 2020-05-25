# Generated by Django 3.0.5 on 2020-05-20 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendrier_Conge',
            fields=[
                ('Date_Conge', models.DateField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Conges',
            fields=[
                ('Code_Conges', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Type_Conges', models.CharField(choices=[('Congés Spéciaux', 'Congés Spéciaux'), ('Congés maladie', 'Congés maladie'), ('Repos Sanitaire', 'Repos Sanitaire'), ('Personnel', 'Personnel'), ('Congés annuels', 'Congés annuels'), ('Reprise jours fériés', 'Reprise jours fériés')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('Matricule', models.CharField(default='20200520151335195293', max_length=50, primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50, verbose_name='Nom *')),
                ('Prenom', models.CharField(max_length=50, verbose_name='Prénom(s) *')),
                ('Sexe', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, verbose_name='Sexe *')),
                ('DateDeNaissance', models.DateField(verbose_name='Date de naissance *')),
                ('Adresse', models.CharField(max_length=255, verbose_name='Adresse *')),
                ('Mail', models.EmailField(max_length=254, verbose_name='E-mail *')),
                ('Pays', models.CharField(max_length=30, verbose_name='Pays *')),
                ('Ville', models.CharField(max_length=30, verbose_name='Ville *')),
                ('Mobile', models.CharField(max_length=20, unique=True, verbose_name='Téléphone *')),
                ('Superviseur', models.CharField(blank=True, max_length=100)),
                ('Photo', models.FileField(upload_to='Fichiers/photos', verbose_name='Photo *')),
                ('Type_Utilisateur', models.CharField(choices=[('Stagiaire Pro', 'Stagiaire Pro'), ('Stafiaire académique', 'Stagiaire académique')], max_length=50, verbose_name='Employé(e)/Stagiaire *')),
                ('Filiere', models.CharField(blank=True, max_length=50, verbose_name='Filière *')),
                ('CV', models.FileField(blank=True, upload_to='Fichiers/cv', verbose_name='Curriculum Vitae')),
                ('LettreDeRecommandation', models.FileField(blank=True, upload_to='Fichiers/recommandations', verbose_name='Lettre de recommandation')),
                ('LettreDeMotivation', models.FileField(blank=True, upload_to='Fichiers/motivations', verbose_name='Lettre de motivation')),
                ('CIN', models.CharField(blank=True, help_text="Numéro de votre Carte d'Identité Nationale", max_length=7, unique=True)),
                ('Status_matrimoniel', models.CharField(blank=True, choices=[('Célibataire', 'Célibataire'), ('En couple', 'En couple'), ('Marié(e)', 'Marié(e)'), ('Divorcé(e)', 'Divorcé(e)')], max_length=20, verbose_name='Status matrimoniel')),
                ('Enfants', models.PositiveIntegerField(blank=True, verbose_name='Enfant(s) *')),
                ('Telephone_Fixe', models.CharField(blank=True, max_length=20, verbose_name='Téléphone fixe')),
                ('Departement', models.CharField(choices=[('Direction', 'Direction'), ('Comptabilité', 'Service Comptable'), ('Ressources Humaines', 'Ressources Humaines'), ('Production et Développement', 'Production et Développement'), ('Informatique', 'Service IT'), ('Communication et Marketing', 'Communication et Marketing'), ('Commercial', 'Service Commercial'), ('Juridique', 'Service Juridique')], max_length=50, verbose_name='Département *')),
                ('Fonction', models.CharField(blank=True, choices=[('Dev Front', 'Développeur(euse) Front-End'), ('Dev Back', 'Développeur(euse) Back-End'), ('Dev Full', 'Développeur(euse) Full Stack'), ('Graphiste', 'Graphiste'), ('Maintenancier', 'Maintenancier'), ('CM', 'Community Manager'), ('CC', 'Chargé(e) de Communication'), ('GC', 'Gestionnnaire Comptable'), ('AGC', 'Assistant(e) Gestionnaire Comptable'), ('Audit', 'Auditeur(trice)'), ('Commission', 'Commissaire aux comptes'), ('Juriste', 'Juriste'), ('DRH', 'Directeur(trice) des Ressources Humaines'), ('ARH', 'Assistant(e) de direction des Ressources Humaines'), ('DG', 'Directeur(trice) Général(e)'), ('ADG', 'Assistant(e) de Direction Générale'), ('DC', 'Directeur(trice) Commercial(e)')], max_length=50)),
                ('Lettre_Demande_Emploi', models.FileField(blank=True, upload_to="Fichiers/demandes d'emploi", verbose_name="Lettre de Demande d'Emploi")),
                ('Type_de_Contrat', models.CharField(choices=[('CDD', 'Contrat Durée Déterminée'), ('CDI', 'Contrat Durée Indéterminée'), ('CP', 'Contrat de Prestation'), ('CS', 'Convention de Stage')], max_length=20)),
                ('Date_Entree', models.DateField(blank=True, verbose_name="Date d'entrée *")),
                ('Date_Sortie', models.DateField(blank=True, verbose_name='Date de sortie')),
                ('Nom_Contact_dUrgence', models.CharField(max_length=30, verbose_name="Nom du Contact d'urgence")),
                ('Telephone_Contact_dUrgence', models.CharField(max_length=50, verbose_name="Téléphone du contact d'urgence")),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heureArrivee', models.DateTimeField(verbose_name="Heure d'Arrivée")),
                ('heureDepart', models.DateTimeField(verbose_name='Heure de Départ')),
                ('status', models.CharField(choices=[('avance', 'En avance'), ('retard', 'En retard')], max_length=100)),
                ('debutPause', models.DateTimeField(verbose_name='Heure de début de la Pause')),
                ('finPause', models.DateTimeField(verbose_name='Heure de fin de la Pause')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Utilisateur', verbose_name='Employé')),
            ],
        ),
        migrations.CreateModel(
            name='Prendre_Conge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duree', models.PositiveIntegerField()),
                ('Status', models.CharField(choices=[('En attente', 'En attente'), ('Accordé', 'Accordé'), ('Rejeté', 'Rejeté')], max_length=10)),
                ('conges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Conges')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Calendrier_Conge')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('Code_Permission', models.CharField(auto_created=True, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('Date_Permission', models.DateTimeField(default=django.utils.timezone.now)),
                ('Date_Debut', models.DateField()),
                ('Date_Fin', models.DateField()),
                ('Motif', models.CharField(max_length=50)),
                ('Status', models.CharField(choices=[('Accordée', 'Accordée'), ('En attente', 'En attente'), ('Refusée', 'Refusée')], max_length=10)),
                ('Permissionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Notes_Internes',
            fields=[
                ('Code_Note', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Titre', models.CharField(blank=True, max_length=200)),
                ('Contenu', models.TextField(max_length=2500)),
                ('Destinataire', models.ManyToManyField(related_name='Destinataire', to='utilisateur.Utilisateur')),
                ('Destinateur', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Destinateur', to='utilisateur.Utilisateur')),
            ],
        ),
    ]