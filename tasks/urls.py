from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:id>/delete', views.delete_task, name='delete_task'),
    path('task/<int:id>/update/', views.update_task, name='update_task'),
]

