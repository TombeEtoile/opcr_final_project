from django.urls import resolve, reverse
from oc_lettings_site.views import index


def test_ols_index_url():
    path = reverse('index')
    assert resolve(path).func == index
