# Generated by Django 3.1.4 on 2021-01-14 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_couesetable_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedcoursestable',
            name='id_course',
        ),
        migrations.RemoveField(
            model_name='assignedcoursestable',
            name='id_user',
        ),
        migrations.DeleteModel(
            name='RolesTable',
        ),
        migrations.DeleteModel(
            name='AssignedCoursesTable',
        ),
    ]