# Generated by Django 3.0.8 on 2020-07-19 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0017_auto_20200719_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='Matricule',
            field=models.CharField(default='20200719131910800020', max_length=50, primary_key=True, serialize=False),
        ),
    ]