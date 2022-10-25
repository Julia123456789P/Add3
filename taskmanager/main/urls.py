from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),   #TODO ссылка на все отзывы
    path('about', views.about, name='about'),   #TODO ссылка на контакты
    path('create', views.create, name='create')   #TODO ссылка на добавление отзыва

]
