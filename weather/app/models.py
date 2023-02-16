from django.db import models

# Create your models here.
# one to one model
class User(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    
class Multiple(models.Model):
    images = models.FileField(null=True, blank=True, upload_to="images/")