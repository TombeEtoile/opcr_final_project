"""
Models for the profiles application.

This module defines the Profile model, which represents user profiles
associated with a Django user and includes a favorite city.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
    Represents a user profile, which includes a reference to a Django User
    and the user's favorite city.

    Attributes:
        user (User): A one-to-one relationship with the Django User model.
        favorite_city (str): The user's favorite city, up to 64 characters.
    """
    class Meta:
        """
        Metadata options for the Profile model.
        """
        db_table = 'oc_lettings_site_profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of the profile.

        Returns:
            str: The username associated with the profile.
        """
        return self.user.username
