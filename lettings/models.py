"""
Models for the lettings application.

This module defines the Letting model, which represents a letting
with a title and associated address.
"""

from django.db import models
from oc_lettings_site.models import Address


# Create your models here.
class Letting(models.Model):
    """
    Represents a letting, including a title and an associated address.

    Attributes:
        title (str): The title of the letting, limited to 256 characters.
        address (Address): A one-to-one relationship with the Address model.
    """
    class Meta:
        """
        Metadata options for the Letting model.
        """
        db_table = 'oc_lettings_site_letting'
        verbose_name = 'Letting'
        verbose_name_plural = 'Lettings'

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
