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

class course(models.Model):
    SEMESTER = (
        ('n/a', 'n/a'),
        ('HS19', 'HS19'),
        ('FS20', 'FS20'),
        ('HS20', 'HS20'),
        ('FS21', 'FS21'),
        ('HS21', 'HS21'),
        ('FS22', 'FS22'),
        ('HS22', 'HS22'),
        ('FS23', 'FS23'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    shortname = models.CharField(max_length=10, null=True)
    type = models.ForeignKey(course_type, null=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(course_group, null=True, on_delete=models.SET_NULL)
    credits = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    signed_up = models.CharField(max_length=10, null=True, choices=SEMESTER)
    link = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.name

