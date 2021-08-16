from django.urls import path
from django.views.generic.base import TemplateView
from user_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path ('', views.user , name = 'user'),
    path ('register', views.register, name = 'register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
    