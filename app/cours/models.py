from django.db import models


class kursu(models.Model):
    title = models.CharField('Название курса', max_length=75)
    task = models.TextField('Описание курса', max_length=250)
    teache = models.CharField('Преподаватель', max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/course/{self.id}'

    class Meta:

        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class addtopic(models.Model):
    title = models.CharField('Название темы', max_length=75)
    task = models.TextField('Описание темы', max_length=250)
    kursu_ptr = models.ForeignKey(kursu, on_delete=models.CASCADE)

    def __str__(self):
        return f'Тема {self.title} курса {self.kursu_ptr}'

    def get_absolute_url(self):
        return f'/course/{self.kursu_ptr.id}/{self.id}'

    class Meta:

        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'


class UserTable(models.Model):
    Surname = models.CharField('Фамилия', max_length=30)
    Name = models.CharField('Имя', max_length=30)
    Patromic = models.CharField('Отчество', max_length=40)
    email = models.CharField('E-mail', max_length=40)
    user_status = models.CharField('Статус', max_length=30)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class AssignedCoursesTable(models.Model):
    id_course = models.ManyToManyField(kursu, on_delete=models.CASCADE)
    id_user = models.ManyToManyField(UserTable, on_delete=models.CASCADE)

class TestTable(models.Model):
    id_topic = models.ForeignKey(addtopic, on_delete=models.CASCADE)
    test_name = models.CharField('Название теста', max_length=50)
    time = models.TimeField('Время прохождение')
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

class QuestionsTable(models.Model):
    id_test = models.ForeignKey(TestTable, on_delete=models.CASCADE)
    text = models.CharField('Текст вопроса', max_length=70)
    number = models.IntegerField('Порядковый номер вопроса') # тут я совневаюсь
    ball = models.IntegerField('Балл за ответ')
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class AnswerTable(models.Model):
    id_question = models.ForeignKey(QuestionsTable, on_delete=models.CASCADE)
    text_answer = models.TextField('Ответ на вопрос', max_length=60)
    try_answer = models.BooleanField("Правильный ответ", max_length=60)
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class ExamTable(models.Model):
    id_questions = models.ManyToManyField(QuestionsTable, on_delete=models.CASCADE)
    id_answer = models.ManyToManyField(AnswerTable, on_delete=models.CASCADE)

class ResultsTable(models.Model):
    id_test = models.ManyToManyField(TestTable, on_delete=models.CASCADE)
    id_user = models.ManyToManyField(UserTable, on_delete=models.CASCADE)
    id_exam = models.ManyToManyField(ExamTable, on_delete=models.CASCADE)
    estimation = models.IntegerField()
    timer = models.TimeField()

