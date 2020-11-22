# Generated by Django 3.1.2 on 2020-11-22 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kompetenzen', '0009_auto_20201122_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kompetenzen.course_group'),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kompetenzen.course_type'),
        ),
    ]
