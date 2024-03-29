# Generated by Django 4.1.7 on 2023-04-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_mdpetauthlv2_mdpetauthlv3_joueur_qcmmea1pourcentage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtecContreLesMenacesLv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=255)),
                ('enonce', models.CharField(max_length=255)),
                ('reponse1', models.CharField(max_length=255)),
                ('reponse2', models.CharField(max_length=255)),
                ('reponse3', models.CharField(max_length=255)),
                ('reponce4', models.CharField(max_length=255)),
                ('reponseVrai', models.CharField(max_length=255)),
                ('reponse', models.CharField(max_length=255)),
                ('explication', models.CharField(default='', max_length=1000)),
                ('qcm', models.BooleanField(default=False)),
            ],
        ),
    ]
