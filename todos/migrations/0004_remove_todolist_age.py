# Generated by Django 4.0.5 on 2022-06-15 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todolist_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='age',
        ),
    ]
