from django.urls import path
from App1 import views 

urlpatterns = [
    path('',views.my_todos,name='home'),
    path("add_todo/",views.add_todo,name='add_todo'),
    path("todo_filter/",views.my_todos,name="todo_filter"),
    path("details/<int:id>/",views.todo_details,name="details"),
    path("delete_record/<int:id>/",views.todo_delete,name="delete"),
    path("update_record/<int:pk>/",views.update_todo,name='update_todo'),
    path("feedback/",views.feedback,name='feedback'),
    
    
    
]
