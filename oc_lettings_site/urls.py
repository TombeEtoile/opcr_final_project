"""
URL configuration for the oc_lettings_site application.

This module defines the URL patterns for the main application,
including links to the lettings and profiles applications, as well as the admin panel.
"""

from django.contrib import admin
from django.urls import path, include
from . import views

# from django.urls import path


# def trigger_error(request):
    # division_by_zero = 1 / 0


urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
