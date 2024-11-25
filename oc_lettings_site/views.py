"""
Views for the oc_lettings_site application.

This module contains the view functions for the main index page of the application.
"""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    """
    Renders the main index page of the application.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML for the index page.
    """
    return render(request, 'index.html')
