# Generated by Django 3.0.5 on 2020-07-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0013_auto_20200707_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='statut',
            field=models.CharField(max_length=50, null=True, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200707114809812571', max_length=50, primary_key=True, serialize=False),
        ),
    ]
