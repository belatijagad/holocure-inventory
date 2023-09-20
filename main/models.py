from django.db import models

class Idols(models.Model):
    name = models.CharField(max_length=32)
    branch = models.CharField(max_length=32)
    generation = models.CharField(max_length=32)
    debut_date = models.DateField()
    tagline = models.TextField(max_length=96)
