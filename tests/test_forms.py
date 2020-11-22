import pytest

from kompetenzen.models import *
from kompetenzen.forms import *

# basic check if form is working
@pytest.mark.django_db
def test_kompetenzen_form_valid():
    form_data = {
        "name": "Testkompetenz",
        "shortname": "tko",
        "credits": "3",
    }
    form = CourseForm(data=form_data)
    assert form.is_valid() is True

# check if duplicate value on shortname is detected
@pytest.mark.django_db
def test_kompetenzen_form_invalid():
    course.objects.create(
        name="Testkompetenz",
        shortname="tko",
        credits="3"
    )
    form_data = {
        "name": "Testkompetenz",
        "shortname": "tko",
        "credits": "3",
    }
    form = CourseForm(data=form_data)
    assert form.is_valid() is False
    assert "Shortname ist bereits vorhanden" == form.errors["shortname"][0]