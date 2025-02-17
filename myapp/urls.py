from django.urls import path 
from .views import index, index_with_variables, tasks

urlpatterns = [
    path('index/', index, name="index"),
    path('index/<int:num>/', index_with_variables, name='index_with_variables'),
    path('tasks/', tasks, name="tasks")
]

app_name = "myapp"