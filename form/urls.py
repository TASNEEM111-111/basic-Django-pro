from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('forms/', views.Login_fun, name='Login_fun'),
    path('modelform/', views.LoginForm, name='LoginForm'),
]