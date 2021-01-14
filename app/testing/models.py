from django.db import models
from cours.models import TopicTable
from django.contrib.auth.models import User
# Create your models here.

class TestTable(models.Model):
    id_topic = models.ForeignKey(TopicTable, on_delete=models.CASCADE)
    test_name = models.CharField('Название теста', max_length=50)
    time = models.TimeField('Время прохождение')

    def __str__(self):
        return self.test_name

    def get_absolute_url(self):
        return f'/test/{self.id}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class QuestionsTable(models.Model):
    id_test = models.ForeignKey(TestTable, on_delete=models.CASCADE)
    text = models.CharField('Текст вопроса', max_length=70)
    number = models.IntegerField('Порядковый номер вопроса') # тут я совневаюсь
    ball = models.IntegerField('Балл за ответ')


    def __str__(self):
        return f'Вопрос {self.text} теста {self.id_test}'

    def get_absolute_url(self):
        return f'/test/{self.id_test.id}/{self.id}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'




class AnswerTable(models.Model):
    id_question = models.ForeignKey(QuestionsTable, on_delete=models.CASCADE)
    text_answer = models.TextField('Ответ на вопрос', max_length=60)
    try_answer = models.BooleanField("Правильный ответ", max_length=60)

    def __str__(self):
        return f'Ответ {self.text_answer} на вопрос {self.id_question} теста {self.id_question.id_test}'

    def get_absolute_url(self):
        return f'/test/{self.id_question.id_test.id}/{self.id_question.id}/{self.id}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class ExamTable(models.Model):
    id_questions = models.ForeignKey(QuestionsTable, on_delete=models.CASCADE)
    id_answer = models.ForeignKey(AnswerTable, on_delete=models.CASCADE)



class ResultsTable(models.Model):
    id_test = models.ForeignKey(TestTable, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_exam = models.ForeignKey(ExamTable, on_delete=models.CASCADE)
    estimation = models.IntegerField()
    timer = models.TimeField()

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

