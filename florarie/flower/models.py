from django.db import models

# Create your models here.

class Flower(models.Model):
    nume = models.CharField(max_length=30, default='')
    poza = models.ImageField(default="poze/default.png", upload_to="pictures/", null=True, blank=True)
    pret = models.FloatField()
    descriere = models.TextField()
    stoc = models.PositiveIntegerField(default=0)