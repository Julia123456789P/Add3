from django.db import models
from django.urls import reverse

#TODO модель категорий
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

    #TODO формирование абсолютной ссылки по категориям
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

#TODO модель товаров
class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, verbose_name='Картинка')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    uploaded = models.DateTimeField(auto_now=True, verbose_name='Изменен')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    #TODO формирование абсолютной ссылки на товар
    def get_absolute_url(self):
        return reverse('shop:product', args=[self.id, self.slug])
