# Generated by Django 3.1.2 on 2020-10-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kompetenzen', '0004_auto_20201026_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
