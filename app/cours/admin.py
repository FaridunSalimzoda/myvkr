from django.contrib import admin
from .models import CourseTable, TopicTable

class adminCoursTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'User', 'get_users')
    list_filter =('title', 'task', 'User')

class adminTopicTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'id_course')

admin.site.register(CourseTable, adminCoursTable),
admin.site.register(TopicTable, adminTopicTable),
