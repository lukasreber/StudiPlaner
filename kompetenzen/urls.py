from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('kompetenzen/', views.kompetenzen, name="courses"),
    path('course/<str:pk>/', views.coursedetail, name="coursedetail"),
    path('courseinsert/', views.courseinsert, name="courseinsert"),
    path('courseupdate/<str:pk>/', views.courseupdate, name="courseupdate"),
    path('coursedelete/<str:pk>/', views.coursedelete, name="coursedelete"),
    path('about/', views.about, name="about"),
]