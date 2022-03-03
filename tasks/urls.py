from django.urls import path
from .api import TaskCreateApi, TaskListApi, TaskUpdateApi,TaskDeleteApi
urlpatterns = [
    path('add',TaskCreateApi.as_view()),
    path('',TaskListApi.as_view()),
    path('update/<str:pk>',TaskUpdateApi.as_view()),
    path('delete/<str:pk>',TaskDeleteApi.as_view()),
]