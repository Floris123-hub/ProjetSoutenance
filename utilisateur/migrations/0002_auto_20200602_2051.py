# Generated by Django 3.0.5 on 2020-06-02 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='aujourdhui',
            field=models.DateField(default=datetime.datetime(2020, 6, 2, 20, 51, 41, 892239), verbose_name="Aujourd'hui"),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200602205141889326', max_length=50, primary_key=True, serialize=False),
        ),
    ]
