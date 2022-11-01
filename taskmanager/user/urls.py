from django.urls import path
from . import views


urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='login'),
    path('user_logout', views.user_logout, name='logout'),
    path('zakaz', views.zakaz, name='zakaz')
]