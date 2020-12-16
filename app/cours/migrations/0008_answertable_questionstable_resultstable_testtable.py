# Generated by Django 3.1.2 on 2020-12-12 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0007_assignedcoursestable_usertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50, verbose_name='Название теста')),
                ('time', models.TimeField(verbose_name='Время прохождение')),
                ('id_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.addtopic')),
            ],
        ),
        migrations.CreateModel(
            name='ResultsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.testtable')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=70, verbose_name='Текст вопроса')),
                ('number', models.IntegerField(verbose_name='Порядковый номер вопроса')),
                ('ball', models.IntegerField(verbose_name='Балл за ответ')),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.testtable')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(max_length=60, verbose_name='Ответ на вопрос')),
                ('try_answer', models.BooleanField(max_length=60, verbose_name='Правильный ответ')),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.questionstable')),
            ],
        ),
    ]