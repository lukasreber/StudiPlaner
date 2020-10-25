from django.forms import ModelForm
from .models import *

class CourseInsertForm(ModelForm):
    class Meta:
        model = course
        fields = '__all__'