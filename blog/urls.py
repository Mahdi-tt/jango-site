from django.urls import path
from blog.views import blog_home
from blog.views import blog_single , blog_category ,blog_search
from blog.views import test

app_name='blog'
urlpatterns = [
    path('',blog_home,name='blog_home'),
    path('<int:pid>/',blog_single,name='blog_single'),
    path('category/<str:cat_name>/',blog_home,name='blog_category'),
    path('tag/<str:tag_name>/',blog_home,name='tag'),
    path('author/<str:author_username>/',blog_home,name='blog_author'),
    path('search/',blog_search,name='search'),
    path('test',test,name='test'),
]
