import pytest
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
def test_ols_index_template(client):
    response = client.get('/')
    assert response.templates[0].name == 'index.html'
