
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_home, name='test_home'),
    path('add_test', views.addtest, name = 'addtest'),
    path('<int:pk>/', views.test_dateil, name='test_dateil'),
    path('<int:pk>/add_questions', views.addQuestions, name= 'add_quest'),
    path('<int:pk>/test_update', views.TestUpdateView.as_view(), name='test_update'),
    path('<int:pk>/test_delete', views.TestDeleteView.as_view(), name='test_delete'),
    path('<int:pk>/<int:kk>/', views.question_deteil, name='qust_detele'),
    path('<int:pk>/<int:kk>/quest_update', views.QuestionsUpdateView.as_view(), name = 'quest_update'),
    path('<int:pk>/<int:kk>/quest_delete', views.QuestionsDeleteView.as_view(), name='quest_delete'),
    path('<int:pk>/add_answer', views.addAnswer, name = 'add_answer'),
    path('<int:pk>/<int:kk>/<int:tt>/', views.answer_detele, name='answer_detele'),
    path('<int:pk>/<int:kk>/<int:tt>/answer_delete', views.AnswerDeleteView.as_view(), name='answer_delete'),
    path('<int:pk>/<int:kk>/<int:tt>/answer_update', views.AnswerUpdateView.as_view(), name='answer_update'),
    path('test_user/<int:pk>', views.test_users, name = 'test_user')



]
