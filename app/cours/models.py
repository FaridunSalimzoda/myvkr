from django.db import models


class CoueseTable(models.Model):
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


class TopicTable(models.Model):
    title = models.CharField('Название темы', max_length=75)
    task = models.TextField('Описание темы', max_length=250)
   # kursu_ptr = models.ForeignKey(kursu, on_delete=models.CASCADE)
    id_course = models.ForeignKey(CoueseTable, on_delete=models.CASCADE)
    def __str__(self):
        return f'Тема {self.title} курса {self.id_course}'

    def get_absolute_url(self):
        return f'/course/{self.id_course.id}/{self.id}'

    class Meta:

        verbose_name = 'Тему'
        verbose_name_plural = 'Темы'


class RolesTable(models.Model):
    Surname = models.CharField('Фамилия', max_length=30)
    Name = models.CharField('Имя', max_length=30)
    Patromic = models.CharField('Отчество', max_length=40)
    email = models.CharField('E-mail', max_length=40)
    user_status = models.CharField('Статус', max_length=30)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class AssignedCoursesTable(models.Model):
    id_course = models.ForeignKey(CoueseTable, on_delete=models.CASCADE)
    id_user = models.ForeignKey(RolesTable, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курс'