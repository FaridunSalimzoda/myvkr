
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='testh'),
    path('test', views.addtest, name = 'addtest')
]