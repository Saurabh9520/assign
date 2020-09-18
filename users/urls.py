from django.urls import path

from .views import home_view, signup_view, dashboard_view,new_task,task_list,deleteTask,data
app_name = "users"

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='sign-up'),
    path('dashboard/', dashboard_view, name='dashboard'),
   # path('task/',task_view,name='task'),
   path('delete/', data, name='dashboard'),
    path('task/',task_list,name='table'),
    path('ok2/',new_task),
    path('delete/<str:pk>/',deleteTask,name='delete'),
    ]
