from django.urls import resolve, reverse
from lettings.views import index, letting


def test_lettings_index_url():
    path = reverse('lettings:index')
    assert resolve(path).func == index


def test_letting_detail_url():
    path = reverse('lettings:letting', args=[1])
    assert resolve(path).func == letting
