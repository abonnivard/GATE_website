from django.db import models



class MdpEtAuthLv1(models.Model):
    numero = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255)
    reponse2 = models.CharField(max_length=255)
    reponse3 = models.CharField(max_length=255)
    reponce4 = models.CharField(max_length=255)
    reponseVrai = models.CharField(max_length=255)
    reponse = models.CharField(max_length=255)
    explication = models.CharField(max_length=1000, default='')
    qcm = models.BooleanField(default=False)



class ProtecDesDonneesLv1(models.Model):
    numero = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255)
    reponse2 = models.CharField(max_length=255)
    reponse3 = models.CharField(max_length=255)
    reponce4 = models.CharField(max_length=255)
    reponseVrai = models.CharField(max_length=255)
    reponse = models.CharField(max_length=255)
    explication = models.CharField(max_length=1000, default="")
    qcm = models.BooleanField(default=False)


class ProtecDesDonneesLv2(models.Model):
    numero = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255)
    reponse2 = models.CharField(max_length=255)
    reponse3 = models.CharField(max_length=255)
    reponce4 = models.CharField(max_length=255)
    reponseVrai = models.CharField(max_length=255)
    reponse = models.CharField(max_length=255)
    explication = models.CharField(max_length=1000, default="")
    qcm = models.BooleanField(default=False)

class ProtecDesDonneesLv3(models.Model):
    numero = models.CharField(max_length=255)
    enonce = models.CharField(max_length=255)
    reponse1 = models.CharField(max_length=255)
    reponse2 = models.CharField(max_length=255)
    reponse3 = models.CharField(max_length=255)
    reponce4 = models.CharField(max_length=255)
    reponseVrai = models.CharField(max_length=255)
    reponse = models.CharField(max_length=255)
    explication = models.CharField(max_length=1000, default="")
    qcm = models.BooleanField(default=False)




class Joueur(models.Model):
    username = models.CharField(max_length=255)
    qcmpdd1 = models.FloatField(default=0)
    qcmpdd2 = models.FloatField(default=0)
    qcmpdd3 = models.FloatField(default=0)
    qcmpdd1pourcentage = models.IntegerField(default=0)
    qcmpdd2pourcentage = models.IntegerField(default=0)
    qcmpdd3pourcentage = models.IntegerField(default=0)
    qcmpddTpourcentage = models.IntegerField(default=0)
    validepdd1 = models.BooleanField(default=False)
    validepdd2 = models.BooleanField(default=False)
    validepdd3 = models.BooleanField(default=False)
    validepddT = models.BooleanField(default=False)

