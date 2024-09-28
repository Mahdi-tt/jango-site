from django.db import models
from django.utils import timezone
# Create your models here.
class post(models.Model):
    # author
    # img
    titel= models.CharField(max_length=120)
    content= models.TextField()
    # tag
    # categore
    cuntent_view=models.IntegerField(default=0)
    status= models.BooleanField(default= False)
    publish_date= models.DateTimeField(null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return f"{self.titel} "