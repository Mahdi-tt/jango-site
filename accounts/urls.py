from django.urls import path
from accounts.views import *
from django.contrib.auth import views

app_name = 'accounts'

urlpatterns = [
    #login
    path('login/',login_view, name='login_view'),
    #logout
    path('logout/',logout_view, name='logout_view'),
    #signup
    path('signup/',signup_view, name='signup_view'),
    
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
