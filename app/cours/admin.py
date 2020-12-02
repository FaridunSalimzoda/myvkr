from django.contrib import admin
from .models import kursu
from .models import addtopic
# Register your models here.


admin.site.register(kursu),
admin.site.register(addtopic)