# Generated by Django 3.0.8 on 2020-07-19 11:51

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0014_auto_20200707_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes_internes',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='permission',
            name='Date_Permission',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='presence',
            name='heureArrivee',
            field=models.DateTimeField(verbose_name="Heure d'Arrivée"),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200719125109124257', max_length=50, primary_key=True, serialize=False),
        ),
    ]
