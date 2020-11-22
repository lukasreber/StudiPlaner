#from django.forms import ModelForm
from django import forms

from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'

    def clean_shortname(self):
        shortname = self.cleaned_data.get("shortname")
        for qs in course.objects.all():
            if qs.shortname == shortname:
                raise forms.ValidationError("Shortname ist bereits vorhanden")
        return shortname