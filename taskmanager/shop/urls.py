from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

app_name = 'taskmanager'

urlpatterns = [

    path('', views.product_list, name='product_list'), #TODO ссылка на главную страницу магазина
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),  #TODO товары по категориям
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product')  #TODO ссылка на отдельный товар
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)