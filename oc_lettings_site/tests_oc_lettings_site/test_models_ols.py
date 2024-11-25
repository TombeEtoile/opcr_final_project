import pytest
from oc_lettings_site.models import Address


@pytest.fixture
def address():
    """Fixture pour créer une adresse."""
    return Address.objects.create(
        number=3,
        street="chemin de la petite côte",
        city="Brignais",
        state="France",
        zip_code=3,
        country_iso_code="333"
    )


@pytest.mark.django_db
def test_ols_str(address):
    """
    Teste la méthode __str__ du modèle Profile afin qu'il retourne bien le username.
    """
    # Vérifie que le __str__ retourne le username
    assert str(address) == "3 chemin de la petite côte"
