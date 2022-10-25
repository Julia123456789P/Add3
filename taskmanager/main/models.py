from django.db import models


#TODO таблица с отзывами
class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.title



