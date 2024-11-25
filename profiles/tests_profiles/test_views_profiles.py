import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


# CREATION D'UN FAUX MODELE USER
@pytest.fixture
def user():
    """Fixture pour créer une adresse."""
    return User.objects.create(
        username="TestUser",
        password="Password.123",
        email="test@email.com",
        first_name="John",
        last_name="Doe"
    )


# CREATION D'UN FAUX MODELE PROFILE
@pytest.fixture
def profile(user):
    """Fixture pour créer un profile lié à un user."""
    return Profile.objects.create(user=user, favorite_city="Test favorite_city")


@pytest.mark.django_db
def test_profiles_index(client):
    response = client.get(reverse('profiles:index'))
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_profile_detail(client, user):
    profile = Profile.objects.create(user=user, favorite_city="Test favorite_city")
    response = client.get(reverse('profiles:profile', args=[user.username]))
    assert response.status_code == 200
    assert "Test favorite_city" in response.content.decode()


@pytest.mark.django_db
def test_profiles_index_context(client, profile):
    response = client.get('/profiles/')
    assert 'profiles_list' in response.context
    assert profile in response.context['profiles_list']
