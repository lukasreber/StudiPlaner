import pytest

from django.urls import reverse
from kompetenzen.models import *
from kompetenzen.views import *

def test_always_passes():
    assert True

@pytest.mark.django_db
def test_dashboard_view(client):
    url = reverse("home")
    request = client.get(url)
    response = home(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_kompetenzen_view(client):
    url = reverse("home")
    request = client.get(url)
    response = kompetenzen(request)
    assert response.status_code == 200