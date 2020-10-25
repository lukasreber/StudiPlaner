from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
     done = course.objects.filter(signed_up=TRUE)
     return render(request, 'kompetenzen/dashboard.html')

def kompetenzen(request):
     co = course.objects.all()
     return render(request, 'kompetenzen/kompetenzen.html', {'course':co})

def reports(request):
     return render(request, 'kompetenzen/reports.html')
