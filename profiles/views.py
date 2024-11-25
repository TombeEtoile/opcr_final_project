"""
Views for the profiles application.

This module contains view functions for displaying the list of profiles
and the detailed view for a single profile.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging
import sentry_sdk

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    """
    Renders the main index page of the profiles application.

    Retrieves all profiles from the database and passes them to the template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML for the profiles index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the detailed page for a specific user profile.

    Args:
        request: The HTTP request object.
        username (str): The username of the user whose profile to display.

    Returns:
        HttpResponse: The rendered HTML for the profile detail page.
    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist as e:
        logger.error(f"Profile not found: {username}")
        sentry_sdk.capture_exception(e)
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)
