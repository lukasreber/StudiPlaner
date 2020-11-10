# Generated by Django 3.1.2 on 2020-11-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompetenzen', '0006_auto_20201026_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='course_semester',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('shortname', models.CharField(max_length=4, null=True)),
                ('start', models.DateField(null=True)),
                ('end', models.DateField(null=True)),
                ('current', models.BooleanField(default=False)),
                ('previous', models.BooleanField(default=False)),
                ('start_exam', models.DateField(null=True)),
                ('end_exam', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='signed_up',
        ),
    ]