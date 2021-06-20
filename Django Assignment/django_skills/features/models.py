from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=70)
    contact = models.CharField(max_length=12)
    interests = models.CharField(max_length=80)
