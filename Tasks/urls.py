from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.tasks, name="tasks"),
    path('about_developer', views.about, name="contact"),

    path('task_edit/<str:id>/', views.edit_task, name='task_edit'),
    path('tasks/<str:id>/', views.delete_task, name='tasks'),

    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),

    path('password-reset/', PasswordResetView.as_view(template_name='kalendar/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='kalendar/reset_password_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='kalendar/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='kalendar/password_reset_complete.html'),name='password_reset_complete'),
    path('password-reset/',PasswordResetView.as_view(template_name='users/password_reset.html',html_email_template_name='users/password_reset_email.html'),name='password-reset')]

