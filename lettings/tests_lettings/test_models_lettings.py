import pytest
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
def test_letting_address_relation(letting, address):
    assert letting.address == address


@pytest.mark.django_db
def test_letting_str():
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="City",
        state="ST",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    assert str(letting) == "Test Letting"
