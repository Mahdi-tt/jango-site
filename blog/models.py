from django.db import models

# Create your models here.
class post(models.Model):
    titel= models.CharField(max_length=120)
    content= models.TextField()