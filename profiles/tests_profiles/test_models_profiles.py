import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_user_relation():
    """
    Teste que la relation entre un utilisateur (User) et son profil (Profile)
    est correctement configurée.
    """
    user = User.objects.create_user(
        username="TestUser",
        password="Password.123",
        email="test@email.com",
        first_name="John",
        last_name="Doe"
    )
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    # Vérifie que le profil est lié au bon utilisateur
    assert profile.user == user
    # Vérifie que le champ 'favorite_city' est bien défini
    assert profile.favorite_city == "Paris"


@pytest.mark.django_db
def test_profile_str():
    """
    Teste la méthode __str__ du modèle Profile afin qu'il retourne bien le username.
    """
    user = User.objects.create_user(
        username="TestUser",
        password="Password.123",
        email="test@email.com",
        first_name="John",
        last_name="Doe"
    )
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    # Vérifie que le __str__ retourne le username
    assert str(profile) == "TestUser"
