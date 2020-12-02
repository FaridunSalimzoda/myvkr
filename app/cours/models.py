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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/course/topics/{self.id}'

    class Meta:

        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'