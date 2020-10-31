from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CourseInsertForm
from django.db.models import Sum

def home(request):
     totalcredits = course.objects.aggregate(sumcredits=Sum('credits'))['sumcredits']
     totalcourses = course.objects.count()
     totalcoursegroups = course_group.objects.count()
     coursesdone = course.objects.filter(done=True).count()
     creditsdone = course.objects.filter(done=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
     signedupcurrentsem = course.objects.filter(signed_up='HS20').aggregate(sumcredits=Sum('credits'))['sumcredits']
     perccoursesdone = int((coursesdone / totalcourses * 100))

     groups = course_group.objects.all()

     # getting all information for "Kompetenzgruppen"
     dic = {}
     for group in groups:
          gn = group.name
          # completed credits
          c = course.objects.filter(group__name=gn,done=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
          # percentage done and min percentage left
          if type(c) != int:
               pd = 0
               pl = group.mincredits/group.maxcredits*100
          else:
               pd = c/group.maxcredits*100
               pl = (group.mincredits-c)/group.maxcredits*100
          
          # adding values to dictionary
          dic[gn] = {'credits':c,'max':group.maxcredits,'min':group.mincredits,'percentdone':pd,'percentleft':pl}
     
     context = {
          'totalcoursegroups':totalcoursegroups,
          'totalcourses':totalcourses,
          'totalcredits':totalcredits,
          'coursesdone':coursesdone,
          'creditsdone':creditsdone,
          'perccoursesdone':perccoursesdone,
          'signedupcurrentsem':signedupcurrentsem,
          'groups':groups,
          'dic':dic

          }
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
