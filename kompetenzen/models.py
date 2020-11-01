from django.db import models

# Create your models here.


class course_group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    maxcredits = models.IntegerField(null=True)
    mincredits = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class course_type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class course_semester(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    shortname = models.CharField(max_length=4, null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    current = models.BooleanField(default=False)
    previous = models.BooleanField(default=False)
    start_exam = models.DateField(null=True)
    end_exam = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    shortname = models.CharField(max_length=10, null=True)
    type = models.ForeignKey(course_type, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(course_group, null=True, on_delete=models.SET_NULL)
    credits = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    semester = models.ForeignKey(course_semester, null=True, on_delete=models.SET_NULL, blank=True)
    link = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name

