from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product


#TODO настройка отображениий полей в админке категорий
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # поля в админке
    prepopulated_fields = {'slug': ('name',)}


#TODO настройка отображений полей в адменке товаров
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'available', 'created', 'uploaded'] # поля в админке
    list_filter = ['available', 'created', 'uploaded'] # фильтр
    list_editable = ['price', 'available'] # возможность изменять цену и наличие не заходя в карточку товара
    prepopulated_fields = {'slug': ('name', )}

    #TODO отображение миниатюр картинок в админке ввместо ссылок на картинки
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"

