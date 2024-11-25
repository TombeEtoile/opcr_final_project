import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


# CREATION D'UN FAUX MODELE USER
@pytest.fixture
def user():
    """Fixture pour créer un utilisateur."""
    return User.objects.create(
        username="TestUser",
        password="Password.123",
        email="test@email.com",
        first_name="John",
        last_name="Doe"
    )


@pytest.mark.django_db
def test_profiles_index_template(client):
    response = client.get('/profiles/')
    assert response.templates[0].name == 'profiles/index.html'


@pytest.mark.django_db
def test_profiles_profile_template(client, user):
    profile = Profile.objects.create(user=user, favorite_city="Test City")
    response = client.get(f'/profiles/{profile.user.username}/')
    assert response.templates[0].name == 'profiles/profile.html'
