# Generated by Django 3.1.5 on 2021-01-10 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cours', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.TextField(max_length=60, verbose_name='Ответ на вопрос')),
                ('try_answer', models.BooleanField(max_length=60, verbose_name='Правильный ответ')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='ExamTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.answertable')),
            ],
        ),
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=50, verbose_name='Название теста')),
                ('time', models.TimeField(verbose_name='Время прохождение')),
                ('id_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.topictable')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='ResultsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimation', models.IntegerField()),
                ('timer', models.TimeField()),
                ('id_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.examtable')),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.testtable')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cours.rolestable')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='QuestionsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=70, verbose_name='Текст вопроса')),
                ('number', models.IntegerField(verbose_name='Порядковый номер вопроса')),
                ('ball', models.IntegerField(verbose_name='Балл за ответ')),
                ('id_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.testtable')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='examtable',
            name='id_questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.questionstable'),
        ),
        migrations.AddField(
            model_name='answertable',
            name='id_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testing.questionstable'),
        ),
    ]
