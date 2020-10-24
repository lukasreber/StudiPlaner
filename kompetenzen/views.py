from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'kompetenzen/dashboard.html')

def kompetenzen(request):
     return render(request, 'kompetenzen/kompetenzen.html')

def reports(request):
     return render(request, 'kompetenzen/reports.html')
