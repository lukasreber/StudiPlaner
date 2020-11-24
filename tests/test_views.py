import pytest

from django.urls import reverse
from kompetenzen.models import *
from kompetenzen.views import *

@pytest.mark.django_db
# check for status code 200 and title
def test_dashboard_view(client):
    url = reverse("home")
    request = client.get(url)
    response = home(request)
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "dashboard" in content

@pytest.mark.django_db
def test_kompetenzen_view(client):
    url = reverse("kompetenzen")
    request = client.get(url)
    response = home(request)
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "kompetenzen" in content

# check return on db
@pytest.mark.django_db
def test_kompetenzen_view(client):
    # create a kompetenz entry
    course.objects.create(
        name="Neue Test-Kompetenz",
        shortname="ntk",
        credits="3"
    )
    url = reverse("home")
    request = client.get(url)
    response = kompetenzen(request)
    content = response.content.decode(response.charset)
    assert response.status_code == 200
    assert "ntk" in content