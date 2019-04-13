from django.db import models

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Analysis(models.Model):
    location = models.CharField(max_length=40)
    hashtag = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)
    result = models.TextField()
