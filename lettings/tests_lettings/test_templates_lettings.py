import pytest
from oc_lettings_site.models import Address
from lettings.models import Letting


@pytest.mark.django_db
def test_lettings_index_template(client):
    response = client.get('/lettings/')
    assert response.templates[0].name == 'lettings/index.html'


@pytest.mark.django_db
def test_lettings_letting_template(client):
    address = Address.objects.create(
        number=123,
        street="Main Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="USA"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)

    response = client.get(f'/lettings/{letting.id}/')
    assert response.templates[0].name == 'lettings/letting.html'
