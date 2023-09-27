from django.db import models
from django.contrib.auth.models import User

class Idols(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    branch = models.CharField(max_length=32)
    generation = models.CharField(max_length=32)
    debut_date = models.DateField()
    tagline = models.TextField(max_length=96)
    superchats = models.PositiveIntegerField(default=1)
