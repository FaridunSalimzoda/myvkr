from django.contrib import admin
from .models import kursu, addtopic, AssignedCoursesTable, UserTable
# Register your models here.


admin.site.register(kursu),
admin.site.register(addtopic),
admin.site.register(AssignedCoursesTable),
admin.site.register(UserTable)