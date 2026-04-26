from django.urls import path
from . import views
# Или используйте стандартный LogoutView, если предпочитаете
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Здесь должно совпадать с именем функции в views.py
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]