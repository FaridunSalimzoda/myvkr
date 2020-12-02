
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('course/', include('cours.urls')),
    path('test/', include('testing.urls'))
]
