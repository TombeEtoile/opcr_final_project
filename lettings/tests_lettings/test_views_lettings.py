import pytest
from django.urls import reverse
from lettings.models import Letting
from oc_lettings_site.models import Address


# CREATION D'UN FAUX MODELE ADDRESS
@pytest.fixture
def address():
    """Fixture pour créer une adresse."""
    return Address.objects.create(
        number=123,
        street="Main Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="USA"
    )


# CREATION D'UN FAUX MODELE LETTING
@pytest.fixture
def letting(address):
    """Fixture pour créer un letting lié à une adresse."""
    return Letting.objects.create(title="Test Letting", address=address)


@pytest.mark.django_db
def test_lettings_index(client):
    response = client.get(reverse('lettings:index'))
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_letting_detail(client):
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="City",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    response = client.get(reverse('lettings:letting', args=[letting.id]))
    assert response.status_code == 200
    assert "Test Letting" in response.content.decode()


@pytest.mark.django_db
def test_lettings_index_context(client, letting):
    response = client.get('/lettings/')
    assert 'lettings_list' in response.context
    assert letting in response.context['lettings_list']
