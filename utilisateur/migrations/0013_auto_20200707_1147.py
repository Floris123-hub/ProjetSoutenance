# Generated by Django 3.0.5 on 2020-07-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0012_auto_20200707_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prendre_conge',
            name='Status',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Accordé', 'Accordé'), ('Rejeté', 'Rejeté')], max_length=30),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200707114708144517', max_length=50, primary_key=True, serialize=False),
        ),
    ]
