
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='test_home'),
    path('test', views.addtest, name = 'addtest'),
    path('<int:pk>/', views.test_dateil, name='test_dateil'),
    path('<int:pk>/test_update', views.TestUpdateView.as_view(), name='test_update'),
    path('<int:pk>/test_delete', views.TestDeleteView.as_view(), name='test_delete')

]