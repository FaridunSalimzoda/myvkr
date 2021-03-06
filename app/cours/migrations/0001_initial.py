# Generated by Django 3.2 on 2021-05-08 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Название курса')),
                ('task', models.TextField(max_length=250, verbose_name='Описание курса')),
                ('User', models.CharField(max_length=50, verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='TopicTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Название темы')),
                ('task', models.TextField(max_length=250, verbose_name='Описание темы')),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.coursetable')),
            ],
            options={
                'verbose_name': 'Тему',
                'verbose_name_plural': 'Темы',
            },
        ),
    ]
