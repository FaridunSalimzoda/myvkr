from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='ho'),

    path('adt', views.adt, name='adt')
    ]