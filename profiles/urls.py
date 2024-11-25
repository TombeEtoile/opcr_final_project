"""
URL configuration for the profiles application.

This module defines the URL patterns for the profiles application,
including the main index page and detailed profile views.
"""

from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
