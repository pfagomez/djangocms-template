from django.db import models

# Create your models here.

class eintrag(models.Model):
    datum = models.DateTimeField()
    beschreibung = models.CharField(max_length=200)