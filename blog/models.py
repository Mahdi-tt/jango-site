from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class categor(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class post(models.Model):
    author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    img= models.ImageField(upload_to='blog/',default='default.jpg')
    titel= models.CharField(max_length=120)
    content= models.TextField()
    categore= models.ManyToManyField(categor)
    tags = TaggableManager()
    cuntent_view=models.IntegerField(default=0)
    status= models.BooleanField(default= False)
    publish_date= models.DateTimeField(null=True)
    created_date= models.DateTimeField(auto_now_add=True)
    update_date= models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return f"{self.titel} "
    
    def get_absolute_url(self):
        return reverse("blog:blog_single", kwargs={'pid':self.id})
