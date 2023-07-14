
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name="home"),
    path('about_developer', views.about, name="contact"),

    path('tasks', views.tasks, name="tasks"),    
    path('task_edit/<str:id>/', views.edit_task, name='task_edit'),
    path('tasks/<str:id>/', views.delete_post, name='tasks'),

    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),

]