# Generated by Django 3.2 on 2021-05-08 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quiz', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='quiz.question')),
                ('answer_order', models.CharField(blank=True, choices=[('content', 'Content'), ('none', 'None')], help_text='Порядок, в котором множественном варианты ответа отображаются для пользователя', max_length=30, null=True, verbose_name='Порядок ответа')),
            ],
            options={
                'verbose_name': 'Вопрос С множественным Выбором',
                'verbose_name_plural': 'Вопросы С множественным Выбором',
            },
            bases=('quiz.question',),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter the answer text that                                             you want displayed', max_length=1000, verbose_name='Content')),
                ('correct', models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcq.mcqquestion', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
