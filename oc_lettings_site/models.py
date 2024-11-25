"""
Models for the oc_lettings_site application.

This module contains the Address model, which is used to represent
the address details in the database.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address with details such as number, street, city, state, zip code, and country ISO code.

    Attributes:
        number (int): The street number, validated to be between 0 and 9999.
        street (str): The name of the street, limited to 64 characters.
        city (str): The name of the city, limited to 64 characters.
        state (str): The two-character state abbreviation.
        zip_code (int): The postal code, validated to be a maximum of 5 digits.
        country_iso_code (str): The three-character ISO code for the country.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a string representation of the address.

        Returns:
            str: The full address as "number street".
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Metadata options for the Address model.
        """
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
