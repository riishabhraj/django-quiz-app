from django.urls import path
from . import views

urlpatterns = [
    path('question_no=<int:question_no>/', views.index, name='game_portal'),
    path('result/', views.result, name='game_result'),
    path('retry/', views.retry, name='game_retry'), 
]
