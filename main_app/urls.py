from django.urls import path
from .views import Home, CreateTaskView,EditTaskView,DeleteTaskView,DoneTaskView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create-task/', CreateTaskView.as_view(), name='create_task'),
    path('edit-task/<int:pk>/', EditTaskView.as_view(), name='edit_task'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    path('done-task/<int:pk>/', DoneTaskView.as_view(), name='done-task'),



]
