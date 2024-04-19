from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.task_list, name='task_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('add_task/', views.add_task, name='add_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
