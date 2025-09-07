from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    information = models.CharField(max_length=100)
    review = models.CharField(max_length=80)
    imgs = models.ImageField(upload_to='images/', null=True)

    class Meta:
        db_table = "places"

