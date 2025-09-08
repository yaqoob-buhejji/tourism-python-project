from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    information = models.CharField(max_length=100)
    review = models.CharField(max_length=80)
    imgs = models.ImageField(upload_to='images/', null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    class Meta:
        db_table = "places"

