from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(course)
admin.site.register(course_group)
admin.site.register(course_type)
