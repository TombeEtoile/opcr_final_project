from django.urls import resolve, reverse
from profiles.views import index, profile


def test_profiles_index_url():
    path = reverse('profiles:index')
    assert resolve(path).func == index


def test_profile_detail_url():
    path = reverse('profiles:profile', args=[1])
    assert resolve(path).func == profile
