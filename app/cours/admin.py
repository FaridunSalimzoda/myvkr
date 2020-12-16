from django.contrib import admin
from .models import CoueseTable, TopicTable, AssignedCoursesTable,RolesTable , TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable

class adminCoursTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'teache')

class adminTopicTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'id_course')

class adminAssignedCourseTable(admin.ModelAdmin):
    list_display = ('id', 'id_course', 'id_user')

class adminTestTable(admin.ModelAdmin):
    list_display = ('id','id_topic', 'test_name', 'time')

class adminQuestionsTable(admin.ModelAdmin):
    list_display = ('id', 'id_test', 'text', 'number', 'ball')

class adminAnswerTable(admin.ModelAdmin):
    list_display = ('id', 'id_question', 'text_answer', 'try_answer')

class adminExamTable(admin.ModelAdmin):
    list_display = ('id', 'id_questions', 'id_answer')

class adminResultsTable(admin.ModelAdmin):
    list_display = ('id', 'id_test', 'id_user', 'id_exam', 'estimation',
                    'timer')

admin.site.register(CoueseTable, adminCoursTable),
admin.site.register(TopicTable, adminTopicTable),
admin.site.register(AssignedCoursesTable, adminAssignedCourseTable),
admin.site.register(RolesTable),
admin.site.register(TestTable, adminTestTable),
admin.site.register(QuestionsTable, adminQuestionsTable),
admin.site.register(AnswerTable, adminAnswerTable),
admin.site.register(ExamTable, adminExamTable),
admin.site.register(ResultsTable, adminResultsTable)