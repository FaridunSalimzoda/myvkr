from django.contrib import admin
from .models import CoueseTable, TopicTable, AssignedCoursesTable,RolesTable

class adminCoursTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'teache')

class adminTopicTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'id_course')

class adminAssignedCourseTable(admin.ModelAdmin):
    list_display = ('id', 'id_course', 'id_user')

admin.site.register(CoueseTable, adminCoursTable),
admin.site.register(TopicTable, adminTopicTable),
admin.site.register(AssignedCoursesTable, adminAssignedCourseTable),
admin.site.register(RolesTable)