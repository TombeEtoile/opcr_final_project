"""
Views for the lettings application.

This module contains view functions for displaying the list of lettings
and the detailed view for a single letting.
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging
import sentry_sdk

logger = logging.getLogger(__name__)


# Vue pour la page principale des lettings
def index(request):
    """
    Renders the main index page of the lettings application.
    Retrieves all lettings from the database and passes them to the template.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Vue pour la page détaillée d'un letting
def letting(request, letting_id):
    """
    Renders the detailed page for a specific letting.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist as e:
        logger.error(f"Letting not found: {letting_id}")
        sentry_sdk.capture_exception(e)
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sentry_sdk.capture_exception(e)
        return render(request, '500.html', status=500)
