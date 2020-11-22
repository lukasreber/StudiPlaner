from django.forms import ModelForm
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'