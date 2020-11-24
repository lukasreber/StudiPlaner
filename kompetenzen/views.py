from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import CourseForm
from django.db.models import Sum

def percent(n=False,m=False):
     if isinstance(n,int) and isinstance(m,int) and m > 0:
          return int(n/m*100)
     else:
          return 0

def home(request):
     courses             = course.objects.all()
     totalcredits        = sum(d['credits'] for d in courses.values())
     totalcourses        = len(courses)
     totalcoursegroups   = course_group.objects.count()
     coursesdone         = course.objects.filter(done=True).count()
     creditsdone         = sum(d['credits'] for d in courses.values() if d['done']==True)
     signedup            = course.objects.filter(semester__current=True).count()
     creditssignedup     = course.objects.filter(semester__current=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
     perdone             = percent(coursesdone,totalcourses)
     persignedup         = percent(signedup,totalcourses)

     # getting all information for "Kompetenzgruppen"
     groups = course_group.objects.all()
     dic = {}
     for group in groups:
          gn             = group.name
          # completed credits
          c              = course.objects.filter(group__name=gn,done=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
          # currenty signed up credits
          cc             = course.objects.filter(group__name=gn,semester__current=True).aggregate(sumcredits=Sum('credits'))['sumcredits']
          
          # if nothing is returned, change values to zero
          if c is None:
               c = 0
          if cc is None:
               cc = 0

          # percentage done, min percentage left, and signed up percentage
          if c+cc < group.mincredits:
               pd        = percent(c,group.maxcredits)
               pl        = percent(group.mincredits-c-cc,group.maxcredits)
               pc        = percent(cc,group.maxcredits)
          else:
               pd        = percent(c,group.maxcredits)
               pl        = 0
               pc        = percent(cc,group.maxcredits)

          
          
          # adding values to dictionary
          dic[gn] = {
               'credits':c,
               'max':group.maxcredits,
               'min':group.mincredits,
               'percentdone':pd,
               'percentleft':pl,
               'creditscurrent':cc,
               'percentcurrent':pc
               }
     
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
     form = CourseForm()
     if request.method == 'POST':
          form = CourseForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/kompetenzen')
     context = {'form':form}
     return render(request, 'kompetenzen/courseform.html', context)

def courseupdate(request, pk):
     co = course.objects.get(id=pk)
     form = CourseForm(instance=co)

     if request.method == 'POST':
          form = CourseForm(request.POST, instance=co)
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
          cp = course.objects.filter(semester__current=True,type__name='Challenge- / Projektmodul').count()
          cpsum = course.objects.filter(semester__current=True,type__name='Challenge- / Projektmodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
     elif name == "last":
          co = course.objects.filter(semester__previous=True)
          so = course_semester.objects.get(previous=True)
          bo = course.objects.filter(semester__previous=True,type__name='Basismodul').count()
          bosum = course.objects.filter(semester__previous=True,type__name='Basismodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          po = course.objects.filter(semester__previous=True,type__name='Portfoliomodul').count()
          posum = course.objects.filter(semester__previous=True,type__name='Portfoliomodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          cp = course.objects.filter(semester__previous=True,type__name='Challenge- / Projektmodul').count()
          cpsum = course.objects.filter(semester__previous=True,type__name='Challenge- / Projektmodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
     else:
          co = course.objects.all()
          so = course_semester.objects.all()
          bo = course.objects.filter(type__name='Basismodul').count()
          bosum = course.objects.filter(type__name='Basismodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          po = course.objects.filter(type__name='Portfoliomodul').count()
          posum = course.objects.filter(type__name='Portfoliomodul').aggregate(sumcredits=Sum('credits'))['sumcredits']
          cp = course.objects.filter(type__name='Challenge- / Projektmodul').count()
          cpsum = course.objects.filter(type__name='Challenge- / Projektmodul').aggregate(sumcredits=Sum('credits'))['sumcredits']

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
               'posum':posum,
               'cp':cp,
               'cpsum':cpsum
               }
     return render(request, 'kompetenzen/report.html', context)