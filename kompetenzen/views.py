from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CourseInsertForm

def home(request):
     #done = course.objects.filter(signed_up=TRUE)
     return render(request, 'kompetenzen/dashboard.html')

def kompetenzen(request):
     co = course.objects.all()
     return render(request, 'kompetenzen/kompetenzen.html', {'course':co})

def coursedetail(request, pk):
     co = course.objects.get(id=pk)
     context = {'course':co}
     return render(request, 'kompetenzen/course.html', context)

def courseinsert(request):
     form = CourseInsertForm()
     if request.method == 'POST':
          form = CourseInsertForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     
     context = {'form':form}
     return render(request, 'kompetenzen/courseform.html', context)

def courseupdate(request, pk):
     co = course.objects.get(id=pk)
     form = CourseInsertForm(instance=co)

     if request.method == 'POST':
          form = CourseInsertForm(request.POST, instance=co)
          if form.is_valid():
               form.save()
               return redirect('/')

     context = {'form':form}
     return render(request, 'kompetenzen/courseform.html', context)

def coursedelete(request, pk):
     co = course.objects.get(id=pk)
     if request.method == "POST":
          co.delete()
          return redirect('/')
     context = {'co':co}
     return render(request, 'kompetenzen/delete.html', context)

def about(request):
     return render(request, 'kompetenzen/about.html')
