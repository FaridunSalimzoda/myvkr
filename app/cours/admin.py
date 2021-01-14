from django.contrib import admin
from .models import CoueseTable, TopicTable

class adminCoursTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'teache', 'get_users')
    list_filter =('title', 'task', 'teache')

class adminTopicTable(admin.ModelAdmin):
    list_display = ('id', 'title', 'task', 'id_course')

admin.site.register(CoueseTable, adminCoursTable),
admin.site.register(TopicTable, adminTopicTable),
