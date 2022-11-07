from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),   # TODO ссылка на корзину
    path('add/<int:product_id>/',
         views.cart_add,
         name='cart_add'),    # TODO ссылка на добавление товара в корзине
    path('remove/<int:product_id>/',
         views.cart_remove,
         name='cart_remove'),   # TODO ссылка на удаление товара из корзины
    path('zakaz', views.zakaz, name='zakaz')  # TODO ссылка на оформление заказа
]