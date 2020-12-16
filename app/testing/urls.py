
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='test_home'),
    path('test', views.addtest, name = 'addtest')
]