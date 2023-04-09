from django.urls import path
from . import views

urlpatterns = [
    path('poll/<int:id>/', views.AnswerCreateView.as_view(), name='create_answer'),
]