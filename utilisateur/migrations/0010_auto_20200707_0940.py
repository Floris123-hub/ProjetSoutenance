# Generated by Django 3.0.5 on 2020-07-07 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0009_auto_20200624_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='presence',
            name='statut',
            field=models.CharField(max_length=20, null=True, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='Date_Permission',
            field=models.DateField(default=datetime.date(2020, 7, 7)),
        ),
        migrations.AlterField(
            model_name='permission',
            name='Status',
            field=models.CharField(choices=[('Accordée', 'Accordée'), ('En attente', 'En attente'), ('Refusée', 'Refusée')], default='En attente', max_length=10),
        ),
        migrations.AlterField(
            model_name='presence',
            name='aujourdhui',
            field=models.DateField(default=datetime.datetime(2020, 7, 7, 9, 40, 28, 418609), verbose_name="Aujourd'hui"),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200707094028415864', max_length=50, primary_key=True, serialize=False),
        ),
    ]
