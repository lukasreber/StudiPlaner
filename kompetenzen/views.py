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
     signedup = course.objects.filter(semester__current=True).count()
     creditssignedup = course.objects.filter(semester__current=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
     perdone = int((coursesdone / totalcourses * 100))
     persignedup = int((signedup / totalcourses * 100))

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
          'perccoursesdone':perdone,
          'persignedup':persignedup,
          'creditssignedup':creditssignedup,
          'signedup':signedup,
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

def report(request, name):
     if name == "current":
          co = course.objects.filter(semester__current=True)
          so = course_semester.objects.get(current=True)
          bo = course.objects.filter(semester__current=True,type__name='Basismodul').count()
          bosum = course.objects.filter(semester__current=True,type__name='Basismodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          po = course.objects.filter(semester__current=True,type__name='Portfoliomodul').count()
          posum = course.objects.filter(semester__current=True,type__name='Portfoliomodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
     elif name == "last":
          co = course.objects.filter(semester__previous=True)
          so = course_semester.objects.get(previous=True)
          bo = course.objects.filter(semester__current=True,type__name='Basismodul').count()
          bosum = course.objects.filter(semester__current=True,type__name='Basismodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          po = course.objects.filter(semester__current=True,type__name='Portfoliomodul').count()
          posum = course.objects.filter(semester__current=True,type__name='Portfoliomodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
     else:
          co = course.objects.all()
          so = course_semester.objects.all()
          bo = course.objects.filter(semester__current=True,type__name='Basismodul').count()
          bosum = course.objects.filter(semester__current=True,type__name='Basismodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          po = course.objects.filter(semester__current=True,type__name='Portfoliomodul').count()
          posum = course.objects.filter(semester__current=True,type__name='Portfoliomodul').aggregate(sumcredits=Sum('credits'))['sumcredits']

     coursetotal = 0
     creditstotal = 0
     for c in co:
          coursetotal += 1
          creditstotal += c.credits

     context = {'course':co,
               'semester':so,
               'coursetotal':coursetotal,
               'creditstotal':creditstotal,
               'bo':bo,
               'bosum':bosum,
               'po':po,
               'posum':posum
               }
     return render(request, 'kompetenzen/report.html', context)