import pytest
from django.urls import reverse
from oc_lettings_site.models import Address


# CREATION D'UN FAUX MODELE ADRESS
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
def test_ols_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    assert "Welcome to Holiday Homes" in response.content.decode()
