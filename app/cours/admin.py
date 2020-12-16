from django.contrib import admin
from .models import CoueseTable, TopicTable, AssignedCoursesTable,RolesTable , TestTable, QuestionsTable, AnswerTable, ExamTable, ResultsTable

admin.site.register(CoueseTable),
admin.site.register(TopicTable),
admin.site.register(AssignedCoursesTable),
admin.site.register(RolesTable),
admin.site.register(TestTable),
admin.site.register(QuestionsTable),
admin.site.register(AnswerTable),
admin.site.register(ExamTable),
admin.site.register(ResultsTable)