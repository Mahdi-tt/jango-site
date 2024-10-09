from django.urls import path
from blog.views import blog_home
from blog.views import blog_single , blog_category
from blog.views import test

app_name='blog'
urlpatterns = [
    path('',blog_home,name='blog_home'),
    path('<int:pid>/',blog_single,name='blog_single'),
    path('category/<str:cat_name>/',blog_category,name='blog_category'),
    path('test',test,name='test'),
]
