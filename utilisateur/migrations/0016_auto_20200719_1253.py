# Generated by Django 3.0.8 on 2020-07-19 11:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0015_auto_20200719_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes_internes',
            name='Date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200719125350856262', max_length=50, primary_key=True, serialize=False),
        ),
    ]
