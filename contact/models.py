from django import forms
from django.db import models

class ContactModel(models.Model):
    Nom= models.CharField(max_length=20)
    Mail= models.CharField(max_length=20)
    Objet= models.CharField(max_length=30)
    Message= models.TextField(max_length=200, blank=True)


    def __str__(self):
        return self.Nom