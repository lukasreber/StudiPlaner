from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CourseInsertForm
from django.db.models import Sum

def home(request):
     #cosum = course.objects.all().annotate(Sum('credits'))
     totalcredits = course.objects.aggregate(sumcredits=Sum('credits'))['sumcredits']
     done = course.objects.filter(done=True).count()
     group = course_group.objects.all()
     context = {'totalcredits':totalcredits, 'done':done, 'group':group}
     return render(request, 'kompetenzen/dashboard.html', context)

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
               return redirect('/kompetenzen')
     
     context = {'form':form}
     return render(request, 'kompetenzen/courseform.html', context)

def courseupdate(request, pk):
     co = course.objects.get(id=pk)
     form = CourseInsertForm(instance=co)

     if request.method == 'POST':
          form = CourseInsertForm(request.POST, instance=co)
          if form.is_valid():
               form.save()
               return redirect('/kompetenzen')

     context = {'form':form}
     return render(request, 'kompetenzen/courseform.html', context)

def coursedelete(request, pk):
     co = course.objects.get(id=pk)
     if request.method == "POST":
          co.delete()
          return redirect('/kompetenzen')
     context = {'co':co}
     return render(request, 'kompetenzen/delete.html', context)

def about(request):
     return render(request, 'kompetenzen/about.html')
