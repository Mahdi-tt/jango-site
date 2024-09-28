from django.urls import path
from blog.views import blog_home
from blog.views import blog_single
from blog.views import test

app_name='blog'
urlpatterns = [
    path('',blog_home,name='blog_home'),
    path('<int:pid>',blog_single,name='blog_single'),
]
