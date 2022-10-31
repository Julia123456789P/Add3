from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('user/', include('user.urls')),
    path('main/', include('main.urls')),
    path('', include('shop.urls', namespace='shop')),
] #TODO ссылки на все приложения

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
