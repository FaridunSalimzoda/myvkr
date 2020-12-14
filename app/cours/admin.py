from django.contrib import admin
from .models import kursu, addtopic, AssignedCoursesTable, UserTable, TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable

admin.site.register(kursu),
admin.site.register(addtopic),
admin.site.register(AssignedCoursesTable),
admin.site.register(UserTable),
admin.site.register(TestTable),
admin.site.register(QuestionsTable),
admin.site.register(AnswerTable),
admin.site.register(ExamTable),
admin.site.register(ResultsTable)