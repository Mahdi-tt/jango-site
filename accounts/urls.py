from django.urls import path
from accounts.views import *
app_name = 'accounts'

urlpatterns = [
    #login
    path('login/',login_view, name='login_view'),
    #logout
    path('logout/',logout_view, name='logout_view'),
    #signup
    path('signup/',signup_view, name='signup_view'),


]
